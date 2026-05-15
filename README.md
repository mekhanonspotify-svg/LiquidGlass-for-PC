<div align="center">

# 💧 LiquidGlass for PC

A **glassmorphism Spotify desktop remote** inspired by Apple’s **Liquid Glass** design language.

Dynamic blur • Reactive colors • Device switching • Spotify controls • Python + PyWebView

<img src="Images/Screenshot 2026-05-15 144619.png" width="900"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## ✨ Features

- 🎨 Dynamic colors extracted from album artwork
- 💧 Liquid Glass inspired UI with animated blur
- 🎵 Full Spotify playback controls
- 🔁 Shuffle & repeat support
- ⏱ Live playback progress tracking
- 🔊 Volume adjustment
- 🌈 Background blur synced to current track colors
- 🫧 Reactive animated blobs
- 🖥 Spotify device switching support
- ⚡ Auto wake / reconnect inactive Spotify devices
- 🪟 Frameless desktop window with custom controls

---

## 🎬 Demo

<p align="center">
<img src="Images/LG.gif" width="900"/>
</p>

---

## 📸 Screenshots

### Main Interface

<img src="Images/Screenshot 2026-05-15 144619.png" width="900"/>

### Device Switching

<img src="Images/Screenshot 2026-05-15 175020.png" width="900"/>

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC.git
cd LiquidGlass-for-PC
```

Or download the ZIP directly.

---

## 📦 Install Dependencies

Install all requirements:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pywebview requests spotipy PyQt6 colorthief
```

---

## 🔑 Spotify API Setup

Create:

```txt
API.JSON
```

Add your Spotify credentials:

```json
{
  "spotify_id": "YOUR_CLIENT_ID",
  "spotify_secret": "YOUR_CLIENT_SECRET"
}
```

Get credentials from:

https://developer.spotify.com/dashboard

Set Redirect URI:

```txt
http://127.0.0.1:8888/callback
```

---

## ▶ Run the Application

Start:

```bash
python Main.py
```

The first launch opens Spotify authentication.

After connecting, LiquidGlass automatically detects available devices and can transfer playback between them.

---

## 🛠 Built With

- Python
- PyWebView
- PyQt6
- Spotipy
- HTML / CSS / JavaScript
- ColorThief

---

## 🗺 Roadmap

- [ ] Mini mode
- [ ] Lyrics support
- [ ] Better customization
- [ ] Performance improvements
- [ ] More visual effects

---

## 📄 License

Released under the **MIT License**.

---

<div align="center">

### Made with 💖 by **SoulNova**

Inspired by Apple’s Liquid Glass aesthetic.

</div>
