"""
System-wide Speech to Text Tool
Press Ctrl+Shift+Space to start/stop recording
The transcribed text will be typed into whatever input field is active
"""

import sys
import io
import speech_recognition as sr
import keyboard
import pyperclip
import threading
import time
from pynput.keyboard import Controller, Key

# Fix Windows console encoding
if sys.stdout is not None and hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr is not None and hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Initialize
recognizer = sr.Recognizer()
keyboard_controller = Controller()
is_recording = False
recording_thread = None

# Configuration
HOTKEY = 'ctrl+shift+space'  # Change this to your preferred hotkey
LANGUAGE = 'en-US'  # Change to your language: en-US, es-ES, fr-FR, etc.

def type_text(text):
    """Type the text into the active window"""
    # Small delay to ensure the window is ready
    time.sleep(0.1)

    # Type each character
    for char in text:
        keyboard_controller.type(char)

    # Add a space at the end
    keyboard_controller.type(' ')

def record_and_transcribe():
    """Record audio and transcribe to text"""
    global is_recording

    print("🎤 Recording... Press Ctrl+Shift+Space again to stop")

    with sr.Microphone() as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            # Record audio
            audio = recognizer.listen(source, timeout=30, phrase_time_limit=30)

            if not is_recording:  # Check if stopped during recording
                return

            print("🔄 Processing speech...")

            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio, language=LANGUAGE)

            print(f"✅ Transcribed: {text}")

            # Type the text into the active window
            type_text(text)

        except sr.WaitTimeoutError:
            print("⏱️ No speech detected (timeout)")
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")
        except Exception as e:
            print(f"❌ Error: {e}")

    is_recording = False
    print("✋ Stopped recording. Press Ctrl+Shift+Space to record again.")

def toggle_recording():
    """Toggle recording on/off"""
    global is_recording, recording_thread

    if not is_recording:
        is_recording = True
        recording_thread = threading.Thread(target=record_and_transcribe, daemon=True)
        recording_thread.start()
    else:
        is_recording = False
        print("✋ Stopping...")

def main():
    """Main function"""
    print("=" * 60)
    print("🎤 System-wide Speech to Text Tool")
    print("=" * 60)
    print(f"📌 Hotkey: {HOTKEY.upper()}")
    print(f"🌍 Language: {LANGUAGE}")
    print("=" * 60)
    print("\n✅ Ready! Press Ctrl+Shift+Space to start recording")
    print("   The text will be typed into your active window")
    print("   Press Ctrl+C to exit\n")

    # Register the hotkey
    keyboard.add_hotkey(HOTKEY, toggle_recording)

    try:
        # Keep the program running
        keyboard.wait()
    except KeyboardInterrupt:
        print("\n👋 Exiting...")

if __name__ == "__main__":
    main()
