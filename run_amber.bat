@echo off
title Amber Terminal TTS - Vintage Computing
echo.
echo ╔═══════════════════════════════════════════════╗
echo ║  AMBER TERMINAL THEME - CLASSIC UNIX          ║
echo ╚═══════════════════════════════════════════════╝
echo.
echo Starting in AMBER TERMINAL mode...
echo.
echo IMPORTANT: Run this as Administrator!
echo.

cd /d "%~dp0"
python system_speech_amber.py
pause
