@echo off
title Smart Quiz - Public Live Server
echo ============================================================
echo   Smart Quiz - Launching Public Live Website
echo ============================================================
echo.
echo Starting Flask App...
start /b "" "C:\Users\helio\AppData\Local\Programs\Python\Python311\python.exe" app.py
timeout /t 3 /nobreak >nul
echo.
echo Launching Cloudflare Public HTTPS Tunnel...
echo Look for the "https://*.trycloudflare.com" link below!
echo.
if exist ".\cloudflared.exe" (
    .\cloudflared.exe tunnel --url http://127.0.0.1:5000
) else if exist "%LOCALAPPDATA%\cloudflared\cloudflared.exe" (
    "%LOCALAPPDATA%\cloudflared\cloudflared.exe" tunnel --url http://127.0.0.1:5000
) else (
    echo Error: cloudflared.exe not found.
    pause
)
pause
