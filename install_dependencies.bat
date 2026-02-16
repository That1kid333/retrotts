@echo off
echo ===================================
echo Installing Speech to Text Tool
echo ===================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo.
    echo ERROR: Python is not installed!
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo ===================================
echo Installation complete!
echo ===================================
echo.
echo To run the tool, double-click: run_speech_tool.bat
echo Or run: python system_speech_to_text.py
echo.
pause
