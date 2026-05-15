@echo off
title Spotify Remote Dependency Installer
echo ==================================================
echo    Installing Liquid Glass Project Dependencies
echo ==================================================
echo.
echo Addressing "ModuleNotFoundError: No module named 'clr'"...
echo.

:: Upgrade pip first to ensure compatibility with Python 3.14
python -m pip install --upgrade pip

echo.
echo Installing: pywebview, pythonnet, spotipy, requests, colorthief, PyQt6, etc.
echo.

:: Added pythonnet (the fix for the 'clr' error)
pip install pywebview pythonnet spotipy requests colorthief PyQt6 plyer pylrc pygame numpy

echo.
echo ==================================================
echo    Process Finished! 
echo    If you still see 'clr' errors, try restarting 
echo    your IDE (VS Code) to refresh the paths.
echo ==================================================
pause
