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

<img src="Images/Screenshot 2026-05-15 144619.png"/>

---

## 🚀 Installation

Clone:

```bash
git clone https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC.git

cd LiquidGlass-for-PC
```
``or simply download the .zip``


Install dependencies:

```bash
pip install pywebview
pip install requests
pip install spotipy
pip install PyQt6
pip install colorthief
```

or:

```bash
pip install -r requirements.txt
```

---

## 🔑 Spotify API Setup

Create:

```txt
API.JSON
```

Example:

```json
{
"spotify_id":"YOUR_CLIENT_ID",
"spotify_secret":"YOUR_CLIENT_SECRET"
}
```

Get credentials from:

https://developer.spotify.com/dashboard

Redirect URI:

```txt
http://127.0.0.1:8888/callback
```

---

## ▶ Running the App

Start using:

```bash
python main.py
```

or simply **double-click `main.py`** if Python is associated with `.py` files on your system.

On first launch, a browser window will open for **Spotify authentication**.  
Log in and grant access to connect your account.

After authentication, the app will launch automatically.

---

## 🛠 Built With

- Python
- PyWebView
- PyQt6
- Spotipy
- HTML/CSS/JS
- ColorThief

---

## 📌 Roadmap

- [ ] Mini mode
- [ ] Lyrics support

---

## License

MIT License

---

<div align="center">

Made with 💖 by **SoulNova**

</div>
