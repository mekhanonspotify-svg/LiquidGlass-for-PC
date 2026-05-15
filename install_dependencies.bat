@echo off
title Spotify Remote Dependency Installer
echo ==================================================
echo   Installing Liquid Glass Project Dependencies.
echo ==================================================
echo.
echo Installing: pywebview, spotipy, colorthief, PyQt6, requests...
echo.

pip install pywebview spotipy colorthief PyQt6 requests

echo.
echo ==================================================
echo   Process Finished! Check above for any errors.
echo ==================================================
pause
