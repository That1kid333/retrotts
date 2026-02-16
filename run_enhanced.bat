@echo off
echo Starting Enhanced Speech to Text Tool...
echo.
echo Features:
echo  - Visual recording indicator (big red banner)
echo  - Audio beeps when starting/stopping
echo  - Auto-volume ducking (lowers music during recording)
echo.
echo IMPORTANT: Run this as Administrator!
echo (Right-click and select "Run as administrator")
echo.

REM Change to the script's directory
cd /d "%~dp0"

python system_speech_to_text_enhanced.py
pause
