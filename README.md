# 🎵 Liquid Glass Spotify Remote

A sleek **glassmorphic desktop controller** for Spotify with dynamic backgrounds that adapt to your currently playing track’s album art — creating a smooth, immersive "Liquid Glass" experience.

## ✨ Features

- **Dynamic Ambient Backgrounds**  
  Extracts colors from album artwork using ColorThief to generate a vibrant glow that updates with every song.

- **Modern Glassmorphism UI**  
  Frosted-glass inspired interface built with HTML, CSS, and JavaScript.

- **Full Playback Control**  
  Play/pause tracks, skip songs, adjust volume, and toggle shuffle or repeat modes.

- **Real-Time Synchronization**  
  Continuously updates playback progress and status directly from your Spotify account.

---

## ⚠️ Requirements & Notes

- **Internet Connection Required**  
  The app communicates with Spotify's Web API, so an active internet connection is necessary.

- **Performance Considerations**  
  On slower networks, loading album art and metadata may cause delayed UI updates or slower synchronization.

---

# 🚀 Getting Started

## 1. Create Spotify API Credentials

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **Create App**
3. Set the **Redirect URI** to:

```txt
http://127.0.0.1:8888/callback
```

4. Copy your **Client ID** and **Client Secret**

---

## 2. Configure API Credentials

Create a file named:

```txt
API.JSON
```

Place it in the project root directory and add:

```json
{
    "spotify_id": "YOUR_CLIENT_ID_HERE",
    "spotify_secret": "YOUR_CLIENT_SECRET_HERE"
}
```

---

## 3. Install Dependencies

Ensure Python is installed, then run:

```bash
pip install pywebview spotipy colorthief PyQt6 requests
```

Or simply double-click:

```txt
install_dependencies.bat
```

---

## 4. Run the Application

Launch using Python:

```bash
python main.py
```

Or double-click the executable/script file.

---

## 📌 Notes

- Spotify Premium may be required for certain playback controls through the Spotify API.
- Keep your `API.JSON` file private and **never upload it to GitHub**.

---

Enjoy a cleaner, more immersive way to control Spotify 🎧
