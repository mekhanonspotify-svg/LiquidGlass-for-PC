# 🎵 Liquid Glass Spotify Remote

<p align="center">
  <img src="Images/Screenshot%202026-05-15%20144619.png" width="850" alt="Liquid Glass Spotify Remote Screenshot">
</p>

<p align="center">
A sleek <b>glassmorphic desktop controller</b> for Spotify with dynamic backgrounds that adapt to your currently playing track’s album art — creating a smooth, immersive <b>Liquid Glass</b> experience.
</p>

---

## ✨ Features

### 🌈 Dynamic Ambient Backgrounds
Extracts colors from album artwork using **ColorThief** to generate vibrant glowing effects that update with every song.

### 🪟 Modern Glassmorphism UI
Frosted-glass inspired interface built using:

- HTML
- CSS
- JavaScript
- PyWebView

### 🎛 Full Playback Controls

Control Spotify directly:

- ▶ Play / Pause
- ⏭ Skip Tracks
- 🔊 Adjust Volume
- 🔀 Shuffle
- 🔁 Repeat

### ⚡ Real-Time Synchronization
Continuously updates:

- Current track
- Album artwork
- Playback progress
- Device status

---

# ⚠️ Requirements & Notes

### 🌐 Internet Connection Required
The application communicates with Spotify’s Web API.

Without internet access:

- Album artwork won't update
- Playback information won't sync
- Controls may fail

### 🖥 Performance Notes
On slower systems or networks:

- Album art loading may delay
- Dynamic background updates may lag slightly

---

# 🚀 Getting Started

## 1. Create Spotify API Credentials

Go to:

https://developer.spotify.com/dashboard

Then:

1. Click **Create App**
2. Add:

```txt
http://127.0.0.1:8888/callback
```

as your Redirect URI.

3. Copy:

- Client ID
- Client Secret

---

## 2. Configure Credentials

Create:

```txt
API.JSON
```

in the project root.

Add:

```json
{
    "spotify_id": "YOUR_CLIENT_ID_HERE",
    "spotify_secret": "YOUR_CLIENT_SECRET_HERE"
}
```

⚠️ Never upload this file publicly.

Add to `.gitignore`:

```gitignore
API.JSON
```

---

## 3. Install Dependencies

Install manually:

```bash
pip install pywebview spotipy colorthief PyQt6 requests
```

or run:

```txt
install_dependencies.bat
```

---

## 4. Run Application

Launch:

```bash
python main.py
```

Or double-click:

```txt
main.py
```

(or packaged executable if included)

---

# 📦 Dependencies

This project uses:

- PyWebView
- Spotipy
- ColorThief
- PyQt6
- Requests

---

# 📌 Notes

- Spotify Premium may be required for playback controls.
- Keep `API.JSON` private.
- First authentication opens a browser window.

---

# 🛠 Built With

- Python
- HTML
- CSS
- JavaScript
- Spotify Web API
- PyWebView

---

# ❤️ Preview

The UI dynamically adapts to your music, creating an immersive **Liquid Glass** effect inspired by modern translucent interfaces.

---

Enjoy a cleaner, smoother way to control Spotify 🎧
<p align="center">Made with ❤️ by <b>SoulNova</b></p>
