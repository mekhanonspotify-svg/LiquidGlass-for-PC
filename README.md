<div align="center">

# 💧 LiquidGlass for PC

### A glassmorphism Spotify desktop remote inspired by Apple’s Liquid Glass design language

Dynamic blur • Reactive colors • Lyrics • Device switching • Spotify controls

<img width="1918" height="1008" alt="LiquidGlass UI" src="https://github.com/user-attachments/assets/4a7c99e6-585c-4773-9b12-c1b2dbd5bd13"/>

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-WIP-orange)

<br>

A Spotify desktop remote that feels **alive** — with reactive glass effects, dynamic colors, animated backgrounds, and seamless playback control.

⭐ Star the repo if you like it

</div>

---

> ⚠️ **Work in Progress**  
> Expect bugs, active changes, and unfinished features. Stable internet is recommended for smoother syncing.

---

# ✨ Features

### 🎨 Reactive Visuals
- Dynamic colors extracted from album artwork
- Animated **Liquid Glass** blur effects
- Reactive backgrounds & floating UI blobs
- Smooth transitions between tracks

### 🎵 Spotify Controls
- Play / pause / skip
- Volume control
- Shuffle & repeat
- Live playback progress tracking
- Playback transfer between devices

### 📜 Lyrics Support
Uses a custom lyrics API instead of relying solely on Spotify, allowing lyrics for tracks Spotify may not provide.

### 💻 Desktop Experience
- Frameless window
- Custom controls
- Lightweight interface
- Auto reconnect to devices

---

# 🎬 Preview

<p align="center">
<img width="900" src="https://github.com/user-attachments/assets/d9e3428f-8131-4ac1-a7f6-ddec0137754c"/>
</p>

### Main Interface

<img src="https://github.com/user-attachments/assets/a8b2b58d-d49b-4142-a242-c767b5329299"/>

<img src="https://github.com/user-attachments/assets/826a79c8-3bd0-4718-b40c-42391592a021"/>

### Lyrics

<img src="https://github.com/user-attachments/assets/e07793f5-f199-41ce-84bb-af6e9dfb5353"/>

---

# 💻 Compatibility

| Platform | Support |
|----------|----------|
| Windows | ✅ |
| macOS | ❌ |
| Linux | ❌ |

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC.git
cd LiquidGlass-for-PC
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pywebview requests spotipy PyQt6 colorthief
```

Run:

```bash
python Main.py
```

---

## First Launch

The app will automatically open a browser window for Spotify authentication.

After logging in:

1. LiquidGlass detects available devices
2. You can transfer playback
3. Reactive UI updates begin automatically

---

# 📂 Minimal Runtime Files (Optional Cleanup)

Keep:

```txt
Main.py
index.html
API.JSON
```

Also keep any generated authentication/token files.

Safe to remove:

```txt
Images/
README.md
LICENSE
requirements.txt
latest.version
```

---

# 🐞 Known Issues

Current limitations:

- Delayed updates on unstable connections
- Rare freezes/crashes
- Device switching can occasionally lag
- Multi-device syncing still being improved

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

### In Progress

- [ ] Performance optimizations
- [ ] Better multi-device support
- [ ] Improved stability
- [ ] More visual effects

### Planned

- [ ] Mini mode
- [ ] Theme customization
- [ ] Additional animations

---

# 🔮 Upcoming

<img width="1090" src="https://github.com/user-attachments/assets/2e78d457-d0ef-4692-bd35-f1608aba7e83"/>

---

# 🤝 Contributing

Bug reports, ideas, and pull requests are welcome.

If something breaks, open an issue.

If you improve something, submit a PR.

---

# 📄 License

Released under the **MIT License**

---

<div align="center">

### Made with 💖 by **SoulNova**

*"Music controls shouldn't feel static."*

</div>
