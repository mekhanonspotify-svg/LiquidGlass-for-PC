# 🎵 Liquid Glass Remote

Liquid Glass Remote is a sleek, iOS-inspired desktop controller for Spotify. It features a "glassmorphism" interface that dynamically adapts its background colors to match your current track's album art.

---

## ⚠️ Important Requirements

*   **Active WiFi Required:** The app communicates directly with Spotify's API and requires a stable connection.
*   **Connection Speed:** Because the app fetches high-quality art and extracts colors in real-time, **slower WiFi will cause the app to lag behind** or experience delays in updating track info.

---

## 🚀 Setup Instructions

1.  **Install Dependencies:**
    Run this command in your terminal to install the required libraries:
    ```bash
    pip install pywebview spotipy PyQt6 colorthief requests
    
Configure Spotify API:

Go to the Spotify Developer Dashboard.

Create a new App and set the Redirect URI to: http://127.0.0.1:8888/callback

Create a file named API.JSON in your project folder.

Paste your client_id and client_secret into that file (use the JSON format provided below).

Running the App:
Execute the Python script:

Bash
python main.py

    *On the first run, a browser window will open for you to log in and authorize the app.*

---

## 🛠️ Built With
*   **Backend:** Python & Spotipy
*   **Frontend:** HTML5/CSS3 (Liquid Glass UI)
*   **Window Engine:** pywebview & PyQt6
🔑 API.JSON File
Create a file named API.JSON and paste this exact content inside it:

JSON
{
    "spotify_id": "cfe201d7efe34d198cc49964721c0aa3",
    "spotify_secret": "c6cb346940904c8cbd03e92327b9a54c"
}
