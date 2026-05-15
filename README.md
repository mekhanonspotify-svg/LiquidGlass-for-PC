# 🎵 Liquid Glass Spotify Remote

<p align="center">
  <img src="Images/Screenshot%202026-05-15%20144619.png"
       width="900"
       alt="Liquid Glass Spotify Remote"
       style="border-radius:20px;">
</p>

<p align="center">
  <b>A modern glassmorphic Spotify controller with dynamic album-color backgrounds.</b><br>
  Smooth playback controls • Real-time sync • Immersive Liquid Glass visuals
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify API](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

</p>

---

# ✨ Features

### 🌈 Dynamic Ambient Backgrounds
Album artwork colors are extracted using **ColorThief**, generating immersive glowing backgrounds that adapt in real time.

### 🪟 Modern Glassmorphism UI
Built with:

- HTML
- CSS
- JavaScript
- PyWebView

Inspired by modern translucent desktop interfaces.

### 🎛 Playback Controls

| Feature | Support |
|----------|----------|
| Play / Pause | ✅ |
| Skip Tracks | ✅ |
| Volume Control | ✅ |
| Shuffle | ✅ |
| Repeat | ✅ |
| Progress Tracking | ✅ |

---

### ⚡ Real-Time Synchronization

Automatically updates:

- Current track
- Album artwork
- Playback progress
- Device state
- Playback status

---

# ❤️ Why This Exists

Built to make controlling Spotify feel more immersive and visually connected to the music you're listening to.

---

# 🚀 Getting Started

## 1. Create Spotify API Credentials

Visit:

https://developer.spotify.com/dashboard

Create an app and set:

```txt
http://127.0.0.1:8888/callback
```

as your Redirect URI.

Copy:

- Client ID
- Client Secret

---

## 2. Configure Credentials

Create:

```txt
API.JSON
```

Add:

```json
{
  "spotify_id": "YOUR_CLIENT_ID_HERE",
  "spotify_secret": "YOUR_CLIENT_SECRET_HERE"
}
```

Add to `.gitignore`:

```gitignore
API.JSON
```

Never upload API credentials.

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

## 4. Run

Launch:

```bash
python main.py
```

---

# 📦 Dependencies

- PyWebView
- Spotipy
- ColorThief
- PyQt6
- Requests

---

# ⚠️ Notes

### Internet Required
Spotify Web API access requires an active connection.

### Performance
On slower systems:

- Album loading may delay
- Dynamic backgrounds may update slower

### Spotify Premium
Some playback controls may require Premium.

---

# 🗂 Project Structure

```txt
LiquidGlass/
│
├── Images/
│   └── Screenshot.png
│
├── main.py
├── API.JSON
└── install_dependencies.bat

```

---

# 🛠 Built With

- Python
- HTML
- CSS
- JavaScript
- Spotify Web API
- PyWebView

---

# 🗺 Roadmap

- [ ] Lyrics support
- [ ] Mini player mode
- [ ] Additional themes
- [ ] Desktop notifications
- [ ] Visualizer effects
- [ ] Packaged executable releases

---

# 📸 Preview

Dynamic backgrounds adapt to your music, creating an immersive **Liquid Glass** desktop experience.

*(GIF demo coming soon)*

---

<p align="center">
Made with ❤️ by <b>SoulNova</b>
</p>
