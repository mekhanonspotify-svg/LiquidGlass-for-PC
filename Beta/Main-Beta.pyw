import os
import sys
import webview
import json
import ctypes
import time
import requests
import spotipy
import threading
import webbrowser
from spotipy.oauth2 import SpotifyPKCE
from colorthief import ColorThief
from io import BytesIO
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

# --- FIX: Prevent UI from cutting off on scaled monitors (125%, 150% scaling) ---
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

# ==========================================
# CONFIGURATION & VERSIONING
# ==========================================
CURRENT_VERSION = "1.5.6-Beta1"
GITHUB_RAW_VERSION_URL = "https://raw.githubusercontent.com/mekhanonspotify-svg/LiquidGlass-for-PC/main/Beta/latest.version"
GITHUB_REPO_URL = "https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC/tree/main/Beta"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def hide_console():
    """Hides the cmd/terminal window on Windows."""
    hWnd = ctypes.WinDLL('kernel32').GetConsoleWindow()
    if hWnd: ctypes.WinDLL('user32').ShowWindow(hWnd, 0)

def check_for_updates():
    """Fetches the latest version from GitHub and alerts the user if an update is available."""
    try:
        response = requests.get(GITHUB_RAW_VERSION_URL, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            
            current_tuple = tuple(map(int, CURRENT_VERSION.split('.')))
            latest_tuple = tuple(map(int, latest_version.split('.')))
            
            if latest_tuple > current_tuple:
                title = "Update Available"
                message = f"There is a new version available!\n\nPlease update to v{latest_version}.\n\nClick OK to visit the GitHub repository."
                result = ctypes.windll.user32.MessageBoxW(0, message, title, 0x1 | 0x40 | 0x40000)
                
                if result == 1:
                    webbrowser.open(GITHUB_REPO_URL)
    except Exception as e:
        print(f"Update check failed: {e}")

# ==========================================
# SPOTIFY BACKEND LOGIC
# ==========================================
class SpotifyRemote:
    def __init__(self):
        self.window = None
        scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        try:
            with open('API.JSON', 'r') as f:
                creds = json.load(f)
                
                auth_manager = SpotifyPKCE(
                    client_id=creds['spotify_id'],
                    redirect_uri="http://127.0.0.1:8888/callback",
                    scope=scope,
                    cache_path=".spotify_cache",
                    open_browser=True
                )
                self.sp = spotipy.Spotify(auth_manager=auth_manager)
        except Exception as e:
            print(f"Auth Error: {e}")
            sys.exit(1)

    def set_window(self, window):
        self.window = window

    def minimize_window(self):
        if self.window: self.window.minimize()

    def toggle_maximize(self):
        if self.window: self.window.toggle_fullscreen()

    def close_window(self):
        if self.window: self.window.destroy()

    def ensure_active(self):
        try:
            pb = self.sp.current_playback()
            if pb is None:
                devices_data = self.sp.devices()
                devices = devices_data.get('devices', []) if devices_data else []
                if devices:
                    self.sp.transfer_playback(device_id=devices[0]['id'], force_play=False)
        except: pass

    def set_device(self, device_id):
        try: self.sp.transfer_playback(device_id=device_id, force_play=False)
        except: pass

    def get_status(self):
        try:
            pb = self.sp.current_playback()
            devices_data = self.sp.devices()
            dev_list = devices_data.get('devices', []) if devices_data else []
            
            clean_devices = [{"id": d['id'], "name": d['name'], "is_active": d['is_active']} for d in dev_list]
            active_device = next((d['name'] for d in dev_list if d['is_active']), "No Device")
            
            if not active_device and dev_list:
                active_device = dev_list[0]['name']

            if pb is None:
                if not dev_list:
                    return {"status": "offline", "devices": [], "active_device": "None"}
                return {"status": "no_track", "devices": clean_devices, "active_device": active_device}

            if pb and pb['item']:
                return {
                    "status": "success",
                    "title": pb['item']['name'],
                    "artist": pb['item']['artists'][0]['name'],
                    "thumb": pb['item']['album']['images'][0]['url'],
                    "time": pb['progress_ms'],
                    "length": pb['item']['duration_ms'],
                    "is_playing": pb['is_playing'],
                    "shuffle": pb['shuffle_state'],
                    "repeat": pb['repeat_state'],
                    "volume": pb['device']['volume_percent'],
                    "devices": clean_devices,
                    "active_device": active_device
                }
            return {"status": "no_track", "devices": clean_devices, "active_device": active_device}
        except:
            return {"status": "offline", "devices": [], "active_device": "None"}

    def get_color_async(self, url, window):
        def _task():
            try:
                res = requests.get(url, timeout=5)
                color = list(ColorThief(BytesIO(res.content)).get_color(quality=5))
                window.evaluate_js(f"updateColors({color})")
            except: pass
        threading.Thread(target=_task, daemon=True).start()

    # --- FIX: Try fetching lyrics up to 3 times ---
    def get_lyrics_async(self, title, artist, window):
        def _task():
            lyrics = "Error fetching lyrics."
            for attempt in range(3):
                try:
                    res = requests.get(f"https://lrclib.net/api/get?track_name={title}&artist_name={artist}", timeout=5)
                    if res.status_code == 200:
                        data = res.json()
                        lyrics = data.get('syncedLyrics') or data.get('plainLyrics') or "No lyrics found for this track."
                        break # Success! Break out of the loop
                    elif res.status_code == 404:
                        lyrics = "No lyrics found for this track."
                        break # Break loop early, track doesn't exist on API
                except Exception:
                    pass
                
                # If we haven't succeeded, wait 1.5 seconds before trying again
                if attempt < 2:
                    time.sleep(1.5)

            window.evaluate_js(f"updateLyrics({json.dumps(lyrics)})")
        threading.Thread(target=_task, daemon=True).start()

    def toggle_audio(self):
        try:
            pb = self.sp.current_playback()
            if pb and pb.get('is_playing'): self.sp.pause_playback()
            elif pb: self.sp.start_playback()
            else:
                self.ensure_active()
                time.sleep(0.5)
                self.sp.start_playback()
        except: pass

    def skip(self, direction):
        try:
            if direction > 0: self.sp.next_track()
            else: self.sp.previous_track()
        except: pass

    def set_time(self, ms):
        try: self.sp.seek_track(int(ms))
        except: pass

    def set_volume(self, vol):
        try: self.sp.volume(int(vol))
        except: pass

    def toggle_shuffle(self):
        try:
            pb = self.sp.current_playback()
            self.sp.shuffle(not pb['shuffle_state'])
        except: pass

    def toggle_repeat(self):
        try:
            pb = self.sp.current_playback()
            modes = {"off": "track", "track": "context", "context": "off"}
            self.sp.repeat(modes[pb['repeat_state']])
        except: pass

# ==========================================
# UI THREADING & STARTUP
# ==========================================
def run_logic(window, api):
    hide_console()
    api.set_window(window)
    api.ensure_active()
    
    threading.Thread(target=check_for_updates, daemon=True).start()
    
    last_track = ""
    offline_check = 0
    
    while True:
        status = api.get_status()
        
        if status["status"] == "success":
            offline_check = 0
            current_track = f"{status['title']}-{status['artist']}"
            if current_track != last_track:
                api.get_color_async(status['thumb'], window)
                api.get_lyrics_async(status['title'], status['artist'], window) # Trigger lyrics fetch
                last_track = current_track
            window.evaluate_js(f"updateUI({json.dumps(status)})")
        
        elif status["status"] == "offline":
            offline_check += 1
            if offline_check >= 3:
                window.evaluate_js("setSystemState('offline')")
        
        elif status["status"] == "no_track":
            window.evaluate_js(f"updateUI({json.dumps(status)})")
            
        time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
    backend = SpotifyRemote()
    
    window = webview.create_window(
        'Liquid Glass Remote', 
        resource_path('index.html'), 
        js_api=backend, 
        width=400, # Increased slightly to prevent tight edges
        height=800,
        background_color='#000000',
        frameless=True,
        easy_drag=False
    )
    
    webview.start(run_logic, (window, backend), gui='qt')
