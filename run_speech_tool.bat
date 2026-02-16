@echo off
echo Starting System-wide Speech to Text Tool...
echo.
echo IMPORTANT: Run this as Administrator for best results!
echo (Right-click and select "Run as administrator")
echo.

REM Change to the script's directory
cd /d "%~dp0"

python system_speech_to_text.py
pause
