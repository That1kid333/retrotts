# 🌃 Retro TTS - Cyberpunk Speech-to-Text Terminal

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗████████╗██████╗  ██████╗     ████████╗████████╗███████╗ ║
║  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝╚══██╔══╝██╔════╝ ║
║  ██████╔╝█████╗     ██║   ██████╔╝██║   ██║       ██║      ██║   ███████╗ ║
║  ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║       ██║      ██║   ╚════██║ ║
║  ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝       ██║      ██║   ███████║ ║
║  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝      ╚═╝   ╚══════╝ ║
╚═══════════════════════════════════════════════════════════════════════╝
```

**A beautiful retro-cyberpunk terminal interface for system-wide speech-to-text on Windows**

[![License: MIT](https://img.shields.io/badge/License-MIT-neon.svg)](LICENSE.txt)
[![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![Python 3.7+](https://img.shields.io/badge/Python-3.7+-brightgreen.svg)](https://www.python.org/)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## ✨ Features

### 🎨 **Stunning Retro UI**
- **Neon cyberpunk color scheme** with bright cyan, magenta, and green
- **ASCII art header** and box-drawing characters
- **Real-time VU meter** with animated audio visualization
- **Blinking recording indicator** - impossible to miss!
- **Smooth 10 FPS UI updates** with Rich library

### 🎤 **Powerful Speech Recognition**
- **System-wide hotkey** - works in ANY application
- **Press once** - speak - auto-detects when you stop
- **Live audio visualization** - see your voice levels
- **Customizable pause detection** - no accidental cutoffs
- **Multi-language support** - English, Spanish, French, German, and more

### 🔊 **Smart Audio Features**
- **Auto-volume ducking** - lowers music while you speak
- **Audio feedback beeps** - know what's happening
- **Microphone monitoring compatible** - hear yourself speak
- **Real-time level meter** - optimal/quiet/loud indicators

### ⚡ **Professional Features**
- **Unlimited recording length** (configurable max time)
- **3-second silence detection** (configurable)
- **Types text into any field** - Word, Chrome, Discord, Slack, etc.
- **Background operation** - minimize and keep working
- **No internet required** for UI (Google Speech API for transcription)

---

## 📥 Installation

### Option 1: Download Executable (Easiest)

1. **Download** the latest release: `RetroTTS-v1.0-Windows.zip`
2. **Extract** the zip file
3. **Right-click** `RetroTTS.exe` → **"Run as administrator"**
4. **Start using it!** Press `Ctrl+Shift+Space` to begin

> ⚠️ **Note:** Must run as administrator for global hotkeys to work

### Option 2: Run from Source

#### Requirements
- Windows 10/11
- Python 3.7 or higher
- Microphone

#### Steps

```bash
# Clone or download this repository
git clone https://github.com/yourusername/retro-tts.git
cd retro-tts

# Install dependencies
pip install -r requirements-desktop.txt

# Run the application
python system_speech_retro.py
```

---

## 🎮 Usage

### Quick Start

1. **Launch** RetroTTS.exe (as administrator)
2. **Minimize** the window if you want
3. **Go to any application** (Word, Chrome, etc.)
4. **Click in a text field**
5. **Press `Ctrl+Shift+Space`**
6. **Speak!** The VU meter shows your voice level
7. **Stop talking** for 3 seconds
8. **Done!** Text appears automatically

### Hotkey

**Default:** `Ctrl+Shift+Space`

### Visual Indicators

- **● READY** (green) - Ready to record
- **● REC** (red, blinking) - Currently recording
- **◐ PROCESSING** (yellow) - Converting speech to text

### VU Meter

```
┤░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒······························├
LEVEL: 65%  OPTIMAL
```

- Green (light shade) - Too quiet, speak up
- Cyan (medium shade) - Optimal volume ✓
- Magenta (full blocks) - Loud, might be too much

---

## ⚙️ Configuration

Edit `system_speech_retro.py` to customize:

### Change Hotkey
```python
HOTKEY = 'ctrl+shift+space'  # Try 'ctrl+alt+s', 'f9', etc.
```

### Adjust Silence Detection
```python
SILENCE_PAUSE = 3.0  # Seconds of silence before stopping (3-5 recommended)
```

### Change Language
```python
LANGUAGE = 'en-US'  # Options: en-GB, es-ES, fr-FR, de-DE, etc.
```

### Modify Max Recording Time
```python
MAX_RECORDING_TIME = 120  # Seconds (120 = 2 minutes)
```

### Customize Colors
```python
COLORS = {
    'neon_cyan': 'bright_cyan',      # Try 'green' for Matrix style
    'neon_magenta': 'bright_magenta', # Or 'bright_white' for minimal
    'neon_green': 'bright_green',     # Change to 'yellow' for amber
}
```

---

## 📸 Screenshots

### Ready State
```
╔═══════════════════════════════════════════════════════════════════════╗
║                        RETRO TTS ASCII LOGO                           ║
╚═══════════════════════════════════════════════════════════════════════╝
┌─────────────────────────┬──────────────────────────────────────────────┐
│ ⚡ SYSTEM STATUS ⚡      │ ▬▬▬ AUDIO INPUT ▬▬▬                         │
│ STATUS: ● READY         │ ┤············································├ │
│ HOTKEY: Ctrl+Shift+Space│ LEVEL: 0%  TOO QUIET                         │
│ LANGUAGE: en-US         ├──────────────────────────────────────────────┤
│ SILENCE: 3.0s           │ ✎ TRANSCRIBED OUTPUT ✎                      │
│ MAX TIME: 120s          │ [ Awaiting input... ]                        │
└─────────────────────────┴──────────────────────────────────────────────┘
```

### Recording State
```
╔═══════════════════════════════════════════════════════════════════════╗
║                        RETRO TTS ASCII LOGO                           ║
╚═══════════════════════════════════════════════════════════════════════╝
┌─────────────────────────┬──────────────────────────────────────────────┐
│ ⚡ SYSTEM STATUS ⚡      │ ▬▬▬ AUDIO INPUT ▬▬▬                         │
│ STATUS: ● REC (blink!)  │ ┤▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒············├ │
│ INFO: Stop talking for  │ LEVEL: 65%  OPTIMAL                          │
│       3s to finish      ├──────────────────────────────────────────────┤
│                         │ ✎ TRANSCRIBED OUTPUT ✎                      │
│                         │ Hello world this is a test                   │
└─────────────────────────┴──────────────────────────────────────────────┘
```

---

## 🛠️ Building from Source

### Create Standalone Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Run the build script
build_release.bat
```

This creates `dist/RetroTTS-v1.0-Windows.zip` ready for distribution!

---

## 🎨 Creating Custom Themes

Want to design your own TUI themes? Here's how:

### 1. Fork this repository
### 2. Modify the color scheme:

```python
COLORS = {
    'neon_cyan': 'your_color_here',
    'neon_magenta': 'your_color_here',
    # ...etc
}
```

### 3. Change the ASCII art header
### 4. Modify the VU meter characters
### 5. Submit a PR or release your own version!

**Available color options:** `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `bright_black`, `bright_red`, `bright_green`, `bright_yellow`, `bright_blue`, `bright_magenta`, `bright_cyan`, `bright_white`

---

## 📋 Requirements

- **OS:** Windows 10 or 11
- **RAM:** 100MB
- **Disk:** 50MB
- **Microphone:** Any USB or built-in mic
- **Internet:** Required for speech recognition API

---

## 🐛 Troubleshooting

### "Permission denied" or hotkey not working
- **Run as administrator** (right-click → Run as administrator)

### "Could not understand audio"
- Check microphone is working and not muted
- Speak more clearly or adjust volume
- Reduce background noise
- Check internet connection

### "PyAudio installation failed"
```bash
pip install pipwin
pipwin install pyaudio
```

### Microphone not detected
- Check Windows sound settings
- Ensure microphone permissions are enabled
- Try unplugging and replugging USB mic

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Ideas for contributions:
- Additional color themes (Matrix green, vaporwave, etc.)
- More language support
- Different ASCII art styles
- Sound effect packs
- UI layout variations
- Performance improvements

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

**TL;DR:** You can use, modify, and distribute this freely, even commercially. Just include the license file.

---

## 🙏 Acknowledgments

- **Rich library** - Beautiful terminal formatting
- **SpeechRecognition** - Google Speech API wrapper
- **PyAudio** - Audio I/O
- **pycaw** - Windows volume control
- Inspired by awesome TUI projects like htop, btop++, and terminal visualizers

### Research Sources:
- [awesome-tuis](https://github.com/rothgar/awesome-tuis)
- [10 Best Python TUI Libraries](https://medium.com/towards-data-engineering/10-best-python-text-user-interface-tui-libraries-for-2025-79f83b6ea16e)
- [Modern TUI Development](https://www.blog.brightcoding.dev/2025/09/07/beyond-the-gui-the-ultimate-guide-to-modern-terminal-user-interface-applications-and-development-libraries/)
- [Cyberpunk ASCII Art Aesthetics](https://asciieverything.com/ascii-tips/ascii-art-in-the-cyberpunk-aesthetic-a-fusion-of-retro-and-futurism/)

---

## 💬 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/retro-tts/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/retro-tts/discussions)

---

<div align="center">

**Made with ❤️ and neo's lights @that1kid333**

**If you like this project, give it a ⭐!**

</div>
