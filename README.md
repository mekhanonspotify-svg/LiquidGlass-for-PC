<div align="center">

# 💧 LiquidGlass for PC

Glassmorphism Spotify remote inspired by Apple’s Liquid Glass design language.

Animated blur • Dynamic colors • Spotify integration • PyWebView + Python

<img src="Images/Screenshot 2026-05-15 144619.png" width="900"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## 🎬 Demo

<video src="Images/LG.mp4" controls width="900"></video>

---

## ✨ Features

- Dynamic colors extracted from album art
- Liquid glass inspired UI
- Spotify playback controls
- Shuffle / Repeat support
- Live playback progress
- Volume control
- Background blur synced with current track
- Animated reactive blobs

---

## 📸 Preview

### Main UI

<img src="Images/Screenshot 2026-05-15 144619.png" width="900"/>

### Alternate View

<img src="Images/Screenshot 2026-05-15 175020.png" width="900"/>

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC.git
cd LiquidGlass-for-PC
````

Or download ZIP.

---

## 📦 Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pywebview
pip install requests
pip install spotipy
pip install PyQt6
pip install colorthief
```

---

## 🔑 Spotify API Setup

Create a file:

```txt
API.JSON
```

Example:

```json
{
  "spotify_id": "YOUR_CLIENT_ID",
  "spotify_secret": "YOUR_CLIENT_SECRET"
}
```

Get credentials:
[https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)

Redirect URI:

```txt
http://127.0.0.1:8888/callback
```

---

## ▶ Running the App

```bash
python main.py
```

Or double-click `main.py`.

First launch will open browser login for Spotify authentication.

---

## 🛠 Built With

* Python
* PyWebView
* PyQt6
* Spotipy
* HTML / CSS / JavaScript
* ColorThief

---

## 📌 Roadmap

* [ ] Mini mode
* [ ] Lyrics support

---

## 📄 License

MIT License

---

<div align="center">

Made with 💖 by **SoulNova**

</div>
