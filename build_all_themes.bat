@echo off
echo ================================================
echo Building ALL Retro TTS Themes
echo ================================================
echo.

cd /d "%~dp0"

echo [1/6] Building CYBERPUNK theme (original)...
pyinstaller --onefile --name "RetroTTS-Cyberpunk" system_speech_retro.py
echo.

echo [2/6] Building MATRIX theme...
pyinstaller --onefile --name "RetroTTS-Matrix" system_speech_matrix.py
echo.

echo [3/6] Building VAPORWAVE theme...
pyinstaller --onefile --name "RetroTTS-Vaporwave" system_speech_vaporwave.py
echo.

echo [4/6] Building AMBER theme...
pyinstaller --onefile --name "RetroTTS-Amber" system_speech_amber.py
echo.

echo [5/6] Building NEON CITY theme...
pyinstaller --onefile --name "RetroTTS-NeonCity" system_speech_neon.py
echo.

echo [6/6] Building MIDNIGHT BLUE theme...
pyinstaller --onefile --name "RetroTTS-MidnightBlue" system_speech_midnight.py
echo.

echo ================================================
echo Creating theme packages...
echo ================================================

cd dist

echo Creating individual theme packages...
powershell Compress-Archive -Path RetroTTS-Cyberpunk.exe -DestinationPath RetroTTS-Cyberpunk-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Matrix.exe -DestinationPath RetroTTS-Matrix-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Vaporwave.exe -DestinationPath RetroTTS-Vaporwave-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Amber.exe -DestinationPath RetroTTS-Amber-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-NeonCity.exe -DestinationPath RetroTTS-NeonCity-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-MidnightBlue.exe -DestinationPath RetroTTS-MidnightBlue-v1.0.zip -Force

echo.
echo Creating MEGA BUNDLE (all themes)...
powershell Compress-Archive -Path *.exe -DestinationPath RetroTTS-AllThemes-v1.0.zip -Force

cd ..

echo.
echo ================================================
echo SUCCESS! All themes packaged!
echo ================================================
echo.
echo Individual themes created:
echo - dist/RetroTTS-Cyberpunk-v1.0.zip
echo - dist/RetroTTS-Matrix-v1.0.zip
echo - dist/RetroTTS-Vaporwave-v1.0.zip
echo - dist/RetroTTS-Amber-v1.0.zip
echo - dist/RetroTTS-NeonCity-v1.0.zip
echo - dist/RetroTTS-MidnightBlue-v1.0.zip
echo.
echo MEGA BUNDLE:
echo - dist/RetroTTS-AllThemes-v1.0.zip (all 6 themes!)
echo.
echo Upload these to streamblur.com!
echo.
pause
