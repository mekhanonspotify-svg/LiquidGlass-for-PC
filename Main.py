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

# ==========================================
# CONFIGURATION & VERSIONING
# ==========================================
CURRENT_VERSION = "1.5.6"
GITHUB_RAW_VERSION_URL = "https://raw.githubusercontent.com/mekhanonspotify-svg/LiquidGlass-for-PC/main/latest.version"
GITHUB_REPO_URL = "https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC/tree/main"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def hide_console():
    if os.name == 'nt':
        hWnd = ctypes.WinDLL('kernel32').GetConsoleWindow()
        if hWnd: ctypes.WinDLL('user32').ShowWindow(hWnd, 0)

def check_for_updates():
    try:
        response = requests.get(GITHUB_RAW_VERSION_URL, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            
            # Convert version strings to tuples for easy comparison (e.g., "1.5.5" -> (1, 5, 5))
            current_tuple = tuple(map(int, CURRENT_VERSION.split('.')))
            latest_tuple = tuple(map(int, latest_version.split('.')))
            
            # 1. Beta Version Check: Current is higher than latest
            if current_tuple > latest_tuple:
                title = "Beta Version"
                message = f"You are currently running a beta version (v{CURRENT_VERSION}). Please expect potential bugs."
                # 0x0 = MB_OK, 0x30 = MB_ICONWARNING, 0x40000 = MB_SYSTEMMODAL
                ctypes.windll.user32.MessageBoxW(0, message, title, 0x0 | 0x30 | 0x40000)

            # 2. Update Check: Latest is higher than current
            elif latest_tuple > current_tuple:
                title = "Update Available"
                message = f"A new version is available!\n\nUpdate to v{latest_version}.\n\nClick OK to visit GitHub."
                # 0x1 = MB_OKCANCEL, 0x40 = MB_ICONINFORMATION, 0x40000 = MB_SYSTEMMODAL
                result = ctypes.windll.user32.MessageBoxW(0, message, title, 0x1 | 0x40 | 0x40000)
                
                # result 1 is IDOK, 2 is IDCANCEL (do nothing if canceled)
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
        self.color_cache = {}
        self.lyrics_cache = {}
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
                self.sp = spotipy.Spotify(auth_manager=auth_manager, retries=3, status_retries=3)
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
                devices = self.sp.devices().get('devices', [])
                if devices:
                    self.sp.transfer_playback(device_id=devices[0]['id'], force_play=False)
        except Exception as e: 
            print(f"Ensure active failed: {e}")

    def set_device(self, device_id):
        try: self.sp.transfer_playback(device_id=device_id, force_play=False)
        except: pass

    def get_status(self):
        try:
            pb = self.sp.current_playback()
            dev_list = self.sp.devices().get('devices', [])
            
            clean_devices = [{"id": d['id'], "name": d['name'], "is_active": d['is_active']} for d in dev_list]
            active_device = next((d['name'] for d in dev_list if d['is_active']), "No Device")
            if not active_device and dev_list: active_device = dev_list[0]['name']

            if pb is None:
                if not dev_list:
                    return {"status": "offline", "devices": [], "active_device": "None"}
                return {"status": "no_track", "devices": clean_devices, "active_device": active_device}

            if pb and pb.get('item'):
                return {
                    "status": "success",
                    "track_id": pb['item']['id'],
                    "title": pb['item']['name'],
                    "artist": pb['item']['artists'][0]['name'],
                    "thumb": pb['item']['album']['images'][0]['url'],
                    "time": pb['progress_ms'],
                    "length": pb['item']['duration_ms'],
                    "is_playing": pb['is_playing'],
                    "shuffle": pb['shuffle_state'],
                    "repeat": pb['repeat_state'],
                    "volume": pb['device']['volume_percent'] if pb.get('device') else 50,
                    "devices": clean_devices,
                    "active_device": active_device
                }
            return {"status": "no_track", "devices": clean_devices, "active_device": active_device}
        except Exception as e:
            return {"status": "offline", "devices": [], "active_device": "None"}

    def get_color_async(self, url, window):
        if url in self.color_cache:
            window.evaluate_js(f"updateColors({self.color_cache[url]})")
            return

        def _task():
            try:
                res = requests.get(url, timeout=5)
                color = list(ColorThief(BytesIO(res.content)).get_color(quality=5))
                self.color_cache[url] = color
                if window: window.evaluate_js(f"updateColors({color})")
            except: pass
        threading.Thread(target=_task, daemon=True).start()

    def get_lyrics_async(self, track_name, artist_name, track_id, window):
        if track_id in self.lyrics_cache:
            if window: window.evaluate_js(f"updateLyrics({json.dumps(self.lyrics_cache[track_id])})")
            return

        def _task():
            try:
                url = "https://lrclib.net/api/get"
                params = {"track_name": track_name, "artist_name": artist_name}
                res = requests.get(url, params=params, timeout=5)
                
                if res.status_code == 200:
                    data = res.json()
                    lyrics = data.get("syncedLyrics") or data.get("plainLyrics") or "No lyrics found."
                else:
                    lyrics = "No lyrics found for this track."
                
                self.lyrics_cache[track_id] = lyrics
                if window: window.evaluate_js(f"updateLyrics({json.dumps(lyrics)})")
            except Exception as e:
                if window: window.evaluate_js(f"updateLyrics('Error connecting to lyrics server.')")
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
    
    last_track_id = None
    offline_check = 0
    
    while True:
        try:
            status = api.get_status()
            
            if status["status"] == "success":
                offline_check = 0
                current_id = status.get('track_id')
                
                if current_id != last_track_id:
                    api.get_color_async(status['thumb'], window)
                    api.get_lyrics_async(status['title'], status['artist'], current_id, window)
                    last_track_id = current_id
                    
                if window: window.evaluate_js(f"updateUI({json.dumps(status)})")
            
            elif status["status"] == "offline":
                offline_check += 1
                if offline_check >= 3 and window:
                    window.evaluate_js("setSystemState('offline')")
            
            elif status["status"] == "no_track" and window:
                window.evaluate_js(f"updateUI({json.dumps(status)})")
        
        except Exception as e:
            print(f"Loop error: {e}")
            
        time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
    backend = SpotifyRemote()
    
    window = webview.create_window(
        'Liquid Glass Remote', 
        resource_path('index.html'), 
        js_api=backend, 
        width=380, 
        height=780,
        background_color='#000000',
        frameless=True,
        easy_drag=False
    )
    
    webview.start(run_logic, (window, backend), gui='qt')
