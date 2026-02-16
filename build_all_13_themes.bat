@echo off
echo ================================================
echo Building ALL 13 Retro TTS Themes
echo ================================================
echo.

cd /d "%~dp0"

REM Original 6 Themes
echo [1/13] Building CYBERPUNK theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Cyberpunk" system_speech_retro.py
echo.

echo [2/13] Building MATRIX theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Matrix" system_speech_matrix.py
echo.

echo [3/13] Building VAPORWAVE theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Vaporwave" system_speech_vaporwave.py
echo.

echo [4/13] Building AMBER theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Amber" system_speech_amber.py
echo.

echo [5/13] Building NEON CITY theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-NeonCity" system_speech_neon.py
echo.

echo [6/13] Building MIDNIGHT BLUE theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-MidnightBlue" system_speech_midnight.py
echo.

REM NEW: PrehiTech Nature Collection
echo [7/13] Building PRIMORDIAL theme (PrehiTech)...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Primordial" system_speech_primordial.py
echo.

echo [8/13] Building DEEP OCEAN theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Ocean" system_speech_ocean.py
echo.

echo [9/13] Building MAGMA theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Magma" system_speech_magma.py
echo.

echo [10/13] Building FOREST DUSK theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Forest" system_speech_forest.py
echo.

echo [11/13] Building GLACIER theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Glacier" system_speech_glacier.py
echo.

echo [12/13] Building DESERT SUNSET theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Desert" system_speech_desert.py
echo.

echo [13/13] Building AURORA BOREALIS theme...
pyinstaller --onefile --hidden-import=pycaw --hidden-import=comtypes --hidden-import=psutil --hidden-import=pyaudio --collect-all speech_recognition --collect-all pycaw --collect-all rich --name "RetroTTS-Aurora" system_speech_aurora.py
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
powershell Compress-Archive -Path RetroTTS-Primordial.exe -DestinationPath RetroTTS-Primordial-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Ocean.exe -DestinationPath RetroTTS-Ocean-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Magma.exe -DestinationPath RetroTTS-Magma-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Forest.exe -DestinationPath RetroTTS-Forest-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Glacier.exe -DestinationPath RetroTTS-Glacier-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Desert.exe -DestinationPath RetroTTS-Desert-v1.0.zip -Force
powershell Compress-Archive -Path RetroTTS-Aurora.exe -DestinationPath RetroTTS-Aurora-v1.0.zip -Force

echo.
echo Creating MEGA BUNDLE (all 13 themes)...
powershell Compress-Archive -Path *.exe -DestinationPath RetroTTS-AllThemes-v2.0.zip -Force

cd ..

echo.
echo ================================================
echo SUCCESS! All 13 themes packaged!
echo ================================================
echo.
echo MEGA BUNDLE:
echo - dist/RetroTTS-AllThemes-v2.0.zip (all 13 themes!)
echo.
echo Individual themes in dist/ folder
echo.
pause
