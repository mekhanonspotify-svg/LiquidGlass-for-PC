<div align="center">

# 💧 LiquidGlass for PC

### A glassmorphism Spotify desktop remote inspired by Apple’s Liquid Glass design language

Dynamic blur • Reactive colors • Playback control • Device switching • Built with Python + PyWebView

<img width="1918" height="1008" alt="LiquidGlass Preview" src="https://github.com/user-attachments/assets/4a7c99e6-585c-4773-9b12-c1b2dbd5bd13" />

<br>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Spotify](https://img.shields.io/badge/API-Spotify-1DB954)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-WIP-orange)

</div>

---

> ⚠️ **Work in Progress**  
> LiquidGlass is actively evolving. Expect bugs, unfinished features, and frequent updates. A stable internet connection is recommended for smooth syncing.

---

# ✨ About

**LiquidGlass for PC** transforms Spotify controls into a dynamic desktop experience using glassmorphism, reactive album colors, animated blur effects, and seamless playback management.

Unlike traditional Spotify remotes, LiquidGlass adapts in real time:

- 🎨 Album artwork color extraction  
- 💧 Liquid-inspired blur effects  
- 🌈 Reactive backgrounds  
- 🫧 Animated UI elements  
- ⚡ Live playback syncing & device transfer  

Built for people who want music controls to feel alive.

---

# 🚀 Features

### 🎵 Playback Controls
- Play / Pause
- Skip & Previous
- Volume adjustment
- Shuffle & Repeat
- Real-time progress tracking

### 🎨 Dynamic Visuals
- Album-based color extraction
- Animated glassmorphism effects
- Reactive backgrounds
- Frameless desktop interface

### 🔄 Device Management
- Switch between Spotify devices
- Auto-detect active sessions
- Wake inactive devices when possible

### 📜 Lyrics *(Experimental)*
Uses an independent lyrics API to provide lyrics beyond Spotify's native availability.

---

# 🎬 Demo & Screenshots

<p align="center">
<img width="900" src="https://github.com/user-attachments/assets/d9e3428f-8131-4ac1-a7f6-ddec0137754c"/>
</p>

## Main Interface

<img width="1918" src="https://github.com/user-attachments/assets/a8b2b58d-d49b-4142-a242-c767b5329299"/>

<br>

<img width="1914" src="https://github.com/user-attachments/assets/826a79c8-3bd0-4718-b40c-42391592a021"/>

---

## Lyrics *(Preview / Under Development)*

<img width="1150" src="https://github.com/user-attachments/assets/e07793f5-f199-41ce-84bb-af6e9dfb5353"/>

---

# 💻 Compatibility

| Platform | Support |
|----------|----------|
| Windows | ✅ |
| macOS | ❌ |
| Linux | ❌ |

---

# 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/mekhanonspotify-svg/LiquidGlass-for-PC.git
cd LiquidGlass-for-PC
```

Or download the ZIP directly from GitHub.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Manual install:

```bash
pip install pywebview requests spotipy PyQt6 colorthief
```

### 3. Run

```bash
python Main.py
```

The first launch opens Spotify authentication in your browser automatically. After signing in, LiquidGlass detects available devices and enables playback transfer.

---

# 📂 Optional Cleanup

For minimal deployment, keep:

✅ Required:

- `Main.py`
- `index.html`
- `API.JSON`

Also keep any generated Spotify authentication files.

Safe to remove:

- `Images/`
- `README.md`
- `LICENSE`
- `requirements.txt`
- `latest.version`

---

# 🐞 Known Issues

Current limitations:

- Occasional playback delay on unstable connections
- Rare freezes/crashes *(restart usually fixes them)*
- Device switching may take additional time
- Cross-device syncing needs refinement

---

# 🛠 Built With

- **Python** → Backend logic
- **PyWebView + PyQt6** → Desktop rendering
- **Spotipy** → Spotify API integration
- **HTML / CSS / JavaScript** → UI
- **ColorThief** → Album color extraction

---

# 🗺 Roadmap

### 🚧 In Progress

- [ ] Lyrics support improvements
- [ ] Performance optimization
- [ ] Better stability
- [ ] Enhanced multi-device support
- [ ] Additional UI effects

### 📌 Planned

- [ ] Mini mode
- [ ] More customization options
- [ ] Expanded platform support

---

# ⬆️ Upcoming Features

### "Begging to update" 😭

<img width="1090" src="https://github.com/user-attachments/assets/2e78d457-d0ef-4692-bd35-f1608aba7e83"/>

---

# 🤝 Contributing

Contributions, ideas, and bug reports are welcome.

Open an issue or submit a pull request to help improve **LiquidGlass**.

---

# 📄 License

Released under the **MIT License**

---

<div align="center">

### Made with 💖 by **SoulNova**

⭐ If you like the project, consider starring the repository.

</div>
