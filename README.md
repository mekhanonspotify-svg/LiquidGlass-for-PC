# 🎵 Liquid Glass Spotify Remote

A sleek, glassmorphic desktop controller for Spotify. This app provides a "Liquid Glass" interface that dynamically adapts its background colors to match the album art of the track currently playing.

## ✨ Features
*   **Dynamic Backgrounds:** Uses ColorThief to extract primary colors from album art for a vibrant, ambient glow.
*   **Glassmorphism UI:** A modern, frosted-glass interface built with HTML/CSS/JS.
*   **Full Control:** Toggle play/pause, skip tracks, adjust volume, and toggle shuffle/repeat.
*   **Real-time Sync:** Tracks progress and playback status directly from your Spotify account.

## ⚠️ Important Requirements
*   **Active Wi-Fi Required:** This app communicates directly with Spotify's Web API. A stable internet connection is mandatory.
*   **Network Performance:** Because the app fetches high-quality album art and metadata, **slower Wi-Fi connections may cause the UI to lag behind** or result in delayed playback updates.

---

## 🚀 Getting Started

### 1. Get Spotify API Credentials
1.  Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2.  Click **Create app**.
3.  Set the **Redirect URI** to: `http://127.0.0.1:8888/callback`
4.  Copy your **Client ID** and **Client Secret**.

### 2. Configuration
Create a file named `API.JSON` in the root folder of the project and paste your credentials:

{
    "spotify_id": "YOUR_CLIENT_ID_HERE",
    "spotify_secret": "YOUR_CLIENT_SECRET_HERE"
}

### 3. Installation
Ensure you have Python installed, then install the dependencies:

```bash
pip install pywebview spotipy colorthief PyQt6 requests
```
4. Running the App
Run the Python script:

```Bash
python main.py
```
---
