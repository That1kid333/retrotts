@echo off
title Retro TTS - Cyberpunk Edition
echo.
echo ╔═══════════════════════════════════════════════╗
echo ║  RETRO-CYBERPUNK SPEECH TO TEXT TERMINAL      ║
echo ╚═══════════════════════════════════════════════╝
echo.
echo Starting in retro mode...
echo.
echo IMPORTANT: Run this as Administrator!
echo (Right-click and select "Run as administrator")
echo.

REM Change to the script's directory
cd /d "%~dp0"

python system_speech_retro.py
pause
