@echo off
title Matrix TTS - The Matrix Has You
echo.
echo ╔═══════════════════════════════════════════════╗
echo ║  MATRIX THEME - GREEN HACKER TERMINAL         ║
echo ╚═══════════════════════════════════════════════╝
echo.
echo Starting in MATRIX mode...
echo.
echo IMPORTANT: Run this as Administrator!
echo (Right-click and select "Run as administrator")
echo.

REM Change to the script's directory
cd /d "%~dp0"

python system_speech_matrix.py
pause
