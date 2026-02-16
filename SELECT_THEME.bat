@echo off
title Retro TTS - Theme Selector

REM Change to script directory
cd /d "%~dp0"

REM Run the beautiful theme selector
python theme_selector.py

REM If Python script exits, close this window
exit
