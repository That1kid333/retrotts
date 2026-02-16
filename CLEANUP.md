# 🧹 Project Cleanup Guide

## Files to KEEP ✅

### Core Application Files:
- `system_speech_retro.py` - Main retro TUI (the star!)
- `system_speech_to_text_enhanced.py` - Enhanced version with visualizer
- `test_speech.py` - Simple test version (useful for troubleshooting)

### Distribution Files:
- `requirements.txt` - Python dependencies
- `README.md` - GitHub documentation
- `LICENSE.txt` - MIT license
- `landing-page.html` - Website landing page

### Documentation:
- `RETRO_TUI_GUIDE.md` - User guide for retro version
- `DISTRIBUTION_GUIDE.md` - How to distribute
- `SETUP_GUIDE.md` - Setup instructions

### Build/Run Scripts:
- `build_release.bat` - Packages for distribution
- `run_retro.bat` - Runs retro version
- `run_enhanced.bat` - Runs enhanced version
- `TEST_SPEECH.bat` - Runs test version

---

## Files to DELETE ❌

### Old/Superseded Files:
1. **speech-to-text.html** - Old browser version (not needed anymore)
2. **system_speech_to_text.py** - Basic version (use enhanced instead)
3. **run_speech_tool.bat** - Old runner for basic version
4. **install_dependencies.bat** - Use `pip install -r requirements.txt` instead
5. **SPEECH_TOOL_README.md** - Old docs (merged into RETRO_TUI_GUIDE.md)
6. **ENHANCED_FEATURES_GUIDE.md** - Info merged into other docs

---

## Quick Cleanup Commands

### Option 1: Manual Deletion
Just delete the 6 files listed above through File Explorer

### Option 2: Batch Script
Run this command (saves a backup first):
```bash
# Creates backup folder
mkdir backup
move speech-to-text.html backup\
move system_speech_to_text.py backup\
move run_speech_tool.bat backup\
move install_dependencies.bat backup\
move SPEECH_TOOL_README.md backup\
move ENHANCED_FEATURES_GUIDE.md backup\
```

---

## Final Clean Structure

```
Presenter2.15.26/
├── Core Apps/
│   ├── system_speech_retro.py (MAIN - Retro TUI)
│   ├── system_speech_to_text_enhanced.py (Enhanced console version)
│   └── test_speech.py (Simple test)
│
├── Themes/ (will be created)
│   ├── system_speech_matrix.py
│   ├── system_speech_vaporwave.py
│   ├── system_speech_amber.py
│   ├── system_speech_neon.py
│   └── system_speech_midnight.py
│
├── Build/Run Scripts/
│   ├── build_release.bat
│   ├── run_retro.bat
│   ├── run_enhanced.bat
│   └── TEST_SPEECH.bat
│
├── Documentation/
│   ├── README.md
│   ├── RETRO_TUI_GUIDE.md
│   ├── DISTRIBUTION_GUIDE.md
│   └── SETUP_GUIDE.md
│
├── Distribution/
│   ├── requirements.txt
│   ├── LICENSE.txt
│   └── landing-page.html
│
└── dist/ (created by build script)
    └── RetroTTS-v1.0-Windows.zip
```

---

**Recommendation:** Delete the old files to keep things clean! ✨
