import os
import sys
import webview
import json
import ctypes
import time
import requests
import spotipy
import threading
from spotipy.oauth2 import SpotifyOAuth
from colorthief import ColorThief
from io import BytesIO
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

def hide_console():
    hWnd = ctypes.WinDLL('kernel32').GetConsoleWindow()
    if hWnd: ctypes.WinDLL('user32').ShowWindow(hWnd, 0)

class SpotifyRemote:
    def __init__(self):
        scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        try:
            with open('API.JSON', 'r') as f:
                creds = json.load(f)
                auth_manager = SpotifyOAuth(
                    client_id=creds['spotify_id'],
                    client_secret=creds['spotify_secret'],
                    redirect_uri="http://127.0.0.1:8888/callback",
                    scope=scope,
                    cache_path=".spotify_cache",
                    open_browser=True
                )
                self.sp = spotipy.Spotify(auth_manager=auth_manager)
        except Exception as e:
            print(f"Auth Error: {e}")
            sys.exit(1)

    def get_status(self):
        try:
            # Check playback
            pb = self.sp.current_playback()
            
            # Persistent check: If pb is None, verify if any device is actually connected
            if pb is None:
                devices = self.sp.devices()
                if not devices['devices']:
                    return {"status": "offline"}
                return {"status": "no_track"}

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
                    "volume": pb['device']['volume_percent']
                }
            return {"status": "no_track"}
        except:
            return {"status": "offline"}

    def get_color_async(self, url, window):
        def _task():
            try:
                res = requests.get(url, timeout=5)
                color = list(ColorThief(BytesIO(res.content)).get_color(quality=5))
                window.evaluate_js(f"updateColors({color})")
            except: pass
        threading.Thread(target=_task, daemon=True).start()

    def toggle_audio(self):
        try:
            pb = self.sp.current_playback()
            if pb['is_playing']: self.sp.pause_playback()
            else: self.sp.start_playback()
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

def run_logic(window, api):
    hide_console()
    last_track = ""
    offline_check = 0
    
    while True:
        status = api.get_status()
        
        if status["status"] == "success":
            offline_check = 0
            current_track = f"{status['title']}-{status['artist']}"
            if current_track != last_track:
                api.get_color_async(status['thumb'], window)
                last_track = current_track
            window.evaluate_js(f"updateUI({json.dumps(status)})")
        
        elif status["status"] == "offline":
            # Buffer the offline state to prevent flickering during pauses
            offline_check += 1
            if offline_check >= 3:
                window.evaluate_js("setSystemState('offline')")
        
        time.sleep(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_ShareOpenGLContexts)
    backend = SpotifyRemote()
    window = webview.create_window(
        'Liquid Glass Remote', 
        'index.html', 
        js_api=backend, 
        width=380, 
        height=740,
        background_color='#000000'
    )
    webview.start(run_logic, (window, backend), gui='qt')
