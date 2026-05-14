# 🎵 Liquid Glass Remote

Liquid Glass Remote is a sleek, iOS-inspired desktop controller for Spotify. Built with Python and modern web technologies, it offers a vibrant, "glassmorphism" interface that dynamically adapts its background colors to match the album art of the music you're currently playing.

---

## ⚠️ Important Requirements

*   **Active WiFi Connection:** This app communicates directly with Spotify's API. A stable internet connection is required for it to function.
*   **Connection Speed:** Because the app fetches high-quality album art and extracts color data in real-time, **slower WiFi connections may cause the UI to lag behind** or experience delays in updating track information.

---

## ✨ Features

*   **Dynamic Color Extraction:** Background gradients change based on the current song's album art.
*   **Full Playback Control:** Play/Pause, Skip, Previous, Shuffle, and Repeat.
*   **Progress Tracking:** Seek through songs using the interactive slider.
*   **Volume Control:** Adjust your Spotify volume directly from the remote.
*   **Glassmorphism UI:** A beautiful, translucent interface with backdrop-blur effects.

---

## 🚀 Setup Instructions

Follow these steps to get the Liquid Glass Remote running on your machine:

### 1. Prerequisites
Ensure you have **Python 3.8+** installed. You will also need a Spotify Premium account (required by the Spotify Web API for playback control).

### 2. Install Dependencies
Run the following command to install the necessary libraries:
```bash
pip install pywebview spotipy PyQt6 colorthief requests
