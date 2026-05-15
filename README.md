---

# 🎵 Liquid Glass Spotify Remote

---

# ✨ Features

### 🌈 Dynamic Ambient Backgrounds

Album artwork colors are extracted using **ColorThief**, generating immersive glowing backgrounds and "liquid blobs" that adapt in real time.

### 🖼️ Mini Player Mode

Switch to a compact, "Always-on-Top" tile mode for a non-intrusive desktop experience. Ideal for keeping your controls visible while working.

### 🎤 Lyrics Support

Slide up the lyrics panel to follow along with your favorite tracks. Features a dedicated translucent interface for focused reading.

### 📊 Visualizer Effects

Dynamic CSS-based audio bars that react when music is playing, adding a rhythmic pulse to the glass interface.

### 🎭 Additional Themes

Choose your vibe with multiple built-in themes:

* **Glass:** The classic translucent look.
* **Midnight:** Deep blues and low-light accents.
* **Retro:** High-contrast orange and monospace aesthetic.

### 🔔 Desktop Notifications

Get system-level toast notifications every time the track changes, so you never have to alt-tab to see what's playing.

---

# 🎛 Playback Controls

| Feature | Support |
| --- | --- |
| Play / Pause | ✅ |
| Skip / Previous | ✅ |
| Volume Control | ✅ |
| Shuffle / Repeat | ✅ |
| Progress Seeking | ✅ |
| Mini Player Mode | ✅ |
| Lyrics Display | ✅ |
| Desktop Toasts | ✅ |

---

# 🚀 Getting Started

## 1. Create Spotify API Credentials

Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
Create an app and set the **Redirect URI** to:
`[http://127.0.0.1:8888/callback](http://127.0.0.1:8888/callback)`

## 2. Configure Credentials

Create a file named `API.JSON` in the root directory:

```json
{
  "spotify_id": "YOUR_CLIENT_ID_HERE",
  "spotify_secret": "YOUR_CLIENT_SECRET_HERE"
}

```

> [!IMPORTANT]
> Never upload your `API.JSON` to public repositories. It is already added to `.gitignore`.

## 3. Install Dependencies

Run the following command to install the required libraries:

```bash
pip install pywebview spotipy requests colorthief PyQt6 plyer pylrc pygame numpy

```

---

# 🗂 Project Structure

```txt
LiquidGlass/
│
├── .spotify_cache        # Generated after first login
├── API.JSON              # Your credentials
├── main.py               # Python Logic (Spotify API + WebView)
├── index.html            # UI/UX (CSS Glassmorphism + JS)
├── install_dependencies.bat
└── Images/
    └── Screenshot.png

```

---

# 🛠 Built With

* **Backend:** Python, Spotipy
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript
* **Engine:** PyWebView (Qt6)
* **Notifications:** Plyer

---

# 🗺 Roadmap

* [x] Lyrics support
* [x] Mini player mode
* [x] Additional themes
* [x] Desktop notifications
* [x] Visualizer effects
* [ ] Packaged executable (.exe) releases
* [ ] Local audio file support

---
