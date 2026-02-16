# 🎤 System-wide Speech to Text Tool

A Windows tool that lets you dictate text into **any application** using a simple hotkey!

## ✨ Features

- **Global hotkey**: Press `Ctrl+Shift+Space` anywhere to start dictating
- **Works in any application**: Word, Excel, Chrome, Notepad, Discord, Slack, etc.
- **Automatic typing**: Transcribed text is typed directly into your active input field
- **Multi-language support**: Easy to configure for different languages
- **Runs in background**: Minimized console window, always ready

## 📋 Requirements

- **Windows 10/11**
- **Python 3.7+** (Download from https://www.python.org/downloads/)
- **Microphone**
- **Internet connection** (for speech recognition API)

## 🚀 Quick Setup

### Step 1: Install Python

1. Download Python from https://www.python.org/downloads/
2. **IMPORTANT**: During installation, check ✅ "Add Python to PATH"
3. Complete the installation

### Step 2: Install Dependencies

1. Double-click `install_dependencies.bat`
2. Wait for all packages to install
3. Close the window when it says "Installation complete"

> **Note**: If you get an error about PyAudio, you may need to install it manually:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

### Step 3: Run the Tool

1. **Right-click** on `run_speech_tool.bat`
2. Select **"Run as administrator"** (required for global hotkeys)
3. Keep the console window open (you can minimize it)

## 🎯 How to Use

1. **Start the tool** using `run_speech_tool.bat` (as administrator)
2. **Click into any text field** (Word, browser, notepad, etc.)
3. **Press `Ctrl+Shift+Space`** to start recording
4. **Speak** into your microphone
5. **Press `Ctrl+Shift+Space` again** to stop and transcribe
6. The text will automatically be typed into your active window!

## ⚙️ Configuration

Edit `system_speech_to_text.py` to customize:

### Change the Hotkey

```python
HOTKEY = 'ctrl+shift+space'  # Change to your preference
```

**Examples**:
- `'ctrl+alt+s'`
- `'ctrl+shift+v'`
- `'alt+space'`

### Change the Language

```python
LANGUAGE = 'en-US'  # Change to your language
```

**Supported languages**:
- `'en-US'` - English (US)
- `'en-GB'` - English (UK)
- `'es-ES'` - Spanish
- `'fr-FR'` - French
- `'de-DE'` - German
- `'it-IT'` - Italian
- `'pt-BR'` - Portuguese
- `'zh-CN'` - Chinese
- `'ja-JP'` - Japanese

## 🔧 Troubleshooting

### "Python is not recognized"
- Reinstall Python and make sure to check "Add Python to PATH"
- Or add Python to PATH manually in System Environment Variables

### "Access Denied" or hotkey not working
- Make sure to **run as administrator**
- Some applications (like certain games) may block keyboard input

### PyAudio installation fails
Run these commands in Command Prompt (as administrator):
```bash
pip install pipwin
pipwin install pyaudio
```

### Microphone not detected
- Check Windows microphone settings
- Ensure microphone permissions are enabled
- Try unplugging and replugging your microphone

### "Could not understand audio"
- Speak more clearly and slowly
- Check your microphone volume
- Reduce background noise
- Ensure you have an internet connection

## 💡 Tips

- **Speak naturally**: No need to speak robotically
- **Punctuation**: Say "period", "comma", "question mark" for punctuation
- **Capitalization**: Say "capital" or "uppercase" before words
- **New line**: Say "new line" or "enter"
- **Keep it running**: Minimize the console window and keep it running in the background

## 🎮 Making it Start Automatically

To have the tool start when Windows boots:

1. Press `Win+R`
2. Type `shell:startup` and press Enter
3. Create a shortcut to `run_speech_tool.bat` in this folder
4. Right-click the shortcut → Properties → Advanced
5. Check "Run as administrator"

## ⚠️ Important Notes

- Requires **internet connection** (uses Google Speech Recognition)
- May have slight delay for processing
- Works best in quiet environments
- Must run as administrator for system-wide hotkeys

## 🛑 Stopping the Tool

Press `Ctrl+C` in the console window, or simply close the window.

## 📝 Examples

1. **Writing an email**: Click in Gmail, press hotkey, dictate your message
2. **Taking notes**: Open Notepad, press hotkey, speak your notes
3. **Coding**: Dictate comments or variable names in your IDE
4. **Messaging**: Use in Discord, Slack, WhatsApp Web, etc.

---

**Enjoy hands-free typing! 🎉**
