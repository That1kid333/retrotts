@echo off
echo ================================================
echo Building Retro TTS Executable
echo ================================================
echo.

REM Change to script directory
cd /d "%~dp0"

echo [1/3] Creating executable with PyInstaller...
pyinstaller --onefile --noconsole --name "RetroTTS" --icon=icon.ico system_speech_retro.py 2>nul
if %errorlevel% neq 0 (
    echo Creating without icon...
    pyinstaller --onefile --noconsole --name "RetroTTS" system_speech_retro.py
)

echo.
echo [2/3] Copying files to dist folder...
copy RETRO_TUI_GUIDE.md dist\ >nul 2>&1
copy LICENSE.txt dist\ >nul 2>&1
copy README.md dist\ >nul 2>&1

echo.
echo [3/3] Creating release package...
cd dist
powershell Compress-Archive -Path * -DestinationPath RetroTTS-v1.0-Windows.zip -Force
cd ..

echo.
echo ================================================
echo SUCCESS! Package created:
echo dist\RetroTTS-v1.0-Windows.zip
echo ================================================
echo.
echo You can now share this zip file!
echo Users just need to:
echo 1. Extract the zip
echo 2. Run RetroTTS.exe as Administrator
echo 3. Enjoy!
echo.
pause
