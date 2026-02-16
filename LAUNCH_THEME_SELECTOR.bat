@echo off
color 0A
title Retro TTS - Theme Selector
cls

:menu
echo.
echo ╔═══════════════════════════════════════════════════════════╗
echo ║                                                           ║
echo ║            RETRO TTS - THEME SELECTOR                     ║
echo ║                                                           ║
echo ╚═══════════════════════════════════════════════════════════╝
echo.
echo   Choose your style:
echo.
echo   [1] CYBERPUNK (Original)    - Cyan/Magenta/Green Neon
echo   [2] MATRIX                  - Classic Green Hacker
echo   [3] VAPORWAVE               - Pink & Cyan A E S T H E T I C
echo   [4] AMBER TERMINAL          - Vintage Unix Computing
echo   [5] NEON CITY               - Rainbow Bright Lights
echo   [6] MIDNIGHT BLUE           - Cool Azure Professional
echo.
echo   [0] EXIT
echo.
echo ═══════════════════════════════════════════════════════════
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto cyberpunk
if "%choice%"=="2" goto matrix
if "%choice%"=="3" goto vaporwave
if "%choice%"=="4" goto amber
if "%choice%"=="5" goto neon
if "%choice%"=="6" goto midnight
if "%choice%"=="0" goto exit
goto invalid

:cyberpunk
cls
echo Starting CYBERPUNK theme...
start run_retro.bat
goto end

:matrix
cls
echo Starting MATRIX theme...
start run_matrix.bat
goto end

:vaporwave
cls
echo Starting VAPORWAVE theme...
start run_vaporwave.bat
goto end

:amber
cls
echo Starting AMBER TERMINAL theme...
start run_amber.bat
goto end

:neon
cls
echo Starting NEON CITY theme...
start run_neon.bat
goto end

:midnight
cls
echo Starting MIDNIGHT BLUE theme...
start run_midnight.bat
goto end

:invalid
echo.
echo Invalid choice! Please enter 1-6.
timeout /t 2 >nul
cls
goto menu

:exit
exit

:end
echo.
echo Theme launcher started!
echo Close this window anytime.
echo.
pause
