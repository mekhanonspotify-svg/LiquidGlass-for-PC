<div align="center">

# 💧 LiquidGlass for PC

A **glassmorphism Spotify desktop remote** inspired by Apple’s **Liquid Glass** design language.

Dynamic blur • Reactive colors • Device switching • Spotify controls • Built with Python + PyWebView

<img src="Images/Screenshot 2026-05-15 144619.png" width="900"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

## ✨ About

**LiquidGlass for PC** is a desktop Spotify remote featuring a **dynamic glassmorphism UI**, reactive colors pulled from album artwork, animated blur effects, and seamless device switching.

Inspired by Apple’s Liquid Glass aesthetic while bringing Spotify controls into a lightweight desktop experience.

---

## 📌 Notes

- 👾 The app may occasionally lag or freeze. Restarting usually fixes the issue.
- 👷 Cross-device support and stability improvements are currently in development.

---

## ⚠️ Important

- 🛜 A stable internet connection is recommended for smooth playback syncing.
- 🌐 Poor or unstable connections may cause delays or incorrect playback updates.

---

# ✨ Features

- 🎨 Dynamic colors extracted from album artwork
- 💧 Liquid Glass-inspired UI with animated blur effects
- 🎵 Full Spotify playback controls
- 🔁 Shuffle & repeat support
- ⏱ Live playback progress tracking
- 🔊 Volume control
- 🌈 Background blur synced with current track colors
- 🫧 Reactive animated blobs
- 🖥 Spotify device switching support
- ⚡ Automatic wake/reconnect for inactive Spotify devices
- 🪟 Frameless desktop window with custom controls

---

# 🎬 Demo

<p align="center">
<img src="Images/LG.gif" width="900"/>
</p>

---

# 📸 Screenshots

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

Or download the ZIP directly from GitHub.

---

## 📦 Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pywebview requests spotipy PyQt6 colorthief
```

---

# 🔑 Spotify API Setup

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

Get your credentials from:

https://developer.spotify.com/dashboard

Set the Redirect URI to:

```txt
http://127.0.0.1:8888/callback
```

Enable:

```txt
• Web API
```

---

# ▶ Running the App

Start LiquidGlass:

```bash
python Main.py
```

On first launch, Spotify authentication will open automatically.

After connecting, LiquidGlass detects available Spotify devices and allows playback transfer between them.

---

# 🛠 Built With

- Python
- PyWebView
- PyQt6
- Spotipy
- HTML / CSS / JavaScript
- ColorThief

---

# 🗺 Roadmap

Planned improvements:

- [ ] Mini mode
- [ ] Lyrics support
- [ ] More customization options
- [ ] Performance optimizations
- [ ] Additional visual effects
- [ ] Improved multi-device support

---

# 🤝 Contributing

Contributions, ideas, and bug reports are welcome.

If you find issues or have suggestions, open an issue or submit a pull request.

---

# 📄 License

Released under the **MIT License**.

---

<div align="center">

## Made with 💖 by **SoulNova**

Inspired by Apple’s Liquid Glass aesthetic.

</div>
