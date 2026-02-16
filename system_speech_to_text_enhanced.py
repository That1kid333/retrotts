"""
Enhanced System-wide Speech to Text Tool
Press Ctrl+Shift+Space to start/stop recording
Features: Visual indicators, volume ducking, beep sounds
"""

import sys
import io
import os
import speech_recognition as sr
import keyboard
import threading
import time
import ctypes
import pyaudio
import struct
import math
from pynput.keyboard import Controller

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
original_volume = None

# Configuration
HOTKEY = 'ctrl+shift+space'  # Change this to your preferred hotkey
LANGUAGE = 'en-US'  # Change to your language: en-US, es-ES, fr-FR, etc.
AUTO_DUCK_VOLUME = True  # Set to False to disable auto-volume ducking
DUCK_PERCENTAGE = 0.3  # Lower volume to 30% when recording (0.0 to 1.0)

# Recording Settings
SILENCE_PAUSE = 3.0  # Seconds of silence before auto-stopping (3-5 recommended)
MAX_RECORDING_TIME = 120  # Maximum recording duration in seconds (120 = 2 minutes)

# Try to import volume control (optional)
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    VOLUME_CONTROL_AVAILABLE = True
except ImportError:
    VOLUME_CONTROL_AVAILABLE = False
    AUTO_DUCK_VOLUME = False

def set_console_title(title):
    """Set the console window title"""
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def beep(frequency=800, duration=100):
    """Play a beep sound"""
    try:
        import winsound
        winsound.Beep(frequency, duration)
    except:
        pass

def get_volume_interface():
    """Get the Windows volume control interface"""
    if not VOLUME_CONTROL_AVAILABLE:
        return None
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume
    except:
        return None

def get_current_volume():
    """Get current system volume (0.0 to 1.0)"""
    volume_interface = get_volume_interface()
    if volume_interface:
        try:
            return volume_interface.GetMasterVolumeLevelScalar()
        except:
            pass
    return None

def set_volume(level):
    """Set system volume (0.0 to 1.0)"""
    volume_interface = get_volume_interface()
    if volume_interface:
        try:
            volume_interface.SetMasterVolumeLevelScalar(level, None)
            return True
        except:
            pass
    return False

def show_recording_banner():
    """Show recording visual indicator"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print("=" * 70)
    print("||" + " " * 66 + "||")
    print("||" + " " * 20 + "🔴 RECORDING NOW 🔴" + " " * 20 + "||")
    print("||" + " " * 66 + "||")
    print("=" * 70)
    print("\n")
    print("  >>> Speak now! Stop talking to finish <<<")
    print("\n")
    if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE:
        print(f"  [Volume lowered to {int(DUCK_PERCENTAGE * 100)}% during recording]")
    print("\n")

def show_audio_level(level):
    """Display real-time audio level bar"""
    # Clear the line and show the audio level
    bar_length = 50
    filled_length = int(bar_length * level)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)

    # Color coding based on level
    if level < 0.3:
        status = "Too quiet"
        color = ""
    elif level < 0.7:
        status = "Good     "
        color = ""
    else:
        status = "Loud     "
        color = ""

    # Print on same line
    print(f"\r  Audio Level: [{bar}] {int(level * 100):3d}% {status}", end='', flush=True)

def show_ready_banner():
    """Show ready visual indicator"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print("=" * 70)
    print("||" + " " * 66 + "||")
    print("||" + " " * 15 + "✅ READY - Press Ctrl+Shift+Space" + " " * 15 + "||")
    print("||" + " " * 66 + "||")
    print("=" * 70)
    print("\n")
    print("  Hotkey: Ctrl+Shift+Space")
    print("  Language: " + LANGUAGE)
    print(f"  Silence pause: {SILENCE_PAUSE}s (stops after this much silence)")
    print(f"  Max recording: {MAX_RECORDING_TIME}s")
    if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE:
        print("  Auto-volume ducking: ENABLED")
    else:
        print("  Auto-volume ducking: DISABLED")
    print("\n  Press Ctrl+C to exit")
    print("\n")

def show_processing_banner():
    """Show processing visual indicator"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print("=" * 70)
    print("||" + " " * 66 + "||")
    print("||" + " " * 20 + "⏳ PROCESSING... ⏳" + " " * 20 + "||")
    print("||" + " " * 66 + "||")
    print("=" * 70)
    print("\n")
    print("  Converting speech to text...")
    print("\n")

def type_text(text):
    """Type the text into the active window"""
    time.sleep(0.1)
    for char in text:
        keyboard_controller.type(char)
    keyboard_controller.type(' ')

def get_rms(data):
    """Calculate RMS (Root Mean Square) of audio data for volume level"""
    try:
        count = len(data) / 2
        format = "%dh" % (count)
        shorts = struct.unpack(format, data)
        sum_squares = sum([sample ** 2 for sample in shorts])
        rms = math.sqrt(sum_squares / count)
        return rms
    except:
        return 0

def record_with_visualization():
    """Record audio with real-time visualization"""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    SILENCE_THRESHOLD = 300  # RMS threshold for detecting speech
    # Use global configuration settings
    SILENCE_DURATION = SILENCE_PAUSE
    MAX_DURATION = MAX_RECORDING_TIME

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    print("\n  🎤 Listening...\n")
    frames = []
    silent_chunks = 0
    started_speaking = False
    chunks_per_second = RATE / CHUNK
    silence_chunks_needed = int(SILENCE_DURATION * chunks_per_second)
    max_chunks = int(MAX_DURATION * chunks_per_second)
    chunk_count = 0

    try:
        while chunk_count < max_chunks:
            data = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(data)
            chunk_count += 1

            # Calculate audio level
            rms = get_rms(data)
            audio_level = min(1.0, rms / 3000)  # Normalize to 0-1

            # Show visual feedback
            show_audio_level(audio_level)

            # Detect speech
            if rms > SILENCE_THRESHOLD:
                started_speaking = True
                silent_chunks = 0
            elif started_speaking:
                silent_chunks += 1
                if silent_chunks > silence_chunks_needed:
                    print("\n")  # New line after the bar
                    break

    except Exception as e:
        print(f"\n  Error recording: {e}\n")
        return None
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    # Convert to audio data for speech recognition
    audio_data = b''.join(frames)
    audio = sr.AudioData(audio_data, RATE, 2)
    return audio

def record_and_transcribe():
    """Record audio and transcribe to text"""
    global is_recording, original_volume

    # Visual and audio feedback
    set_console_title("🔴 RECORDING - Speech to Text")
    show_recording_banner()
    beep(1000, 150)  # High beep for start

    # Lower volume if enabled
    if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE:
        original_volume = get_current_volume()
        if original_volume is not None:
            set_volume(original_volume * DUCK_PERCENTAGE)

    try:
        # Record audio with visualization
        audio = record_with_visualization()

        if audio is None:
            print("\n  ❌ Recording failed\n")
            time.sleep(2)
            is_recording = False
            set_console_title("✅ READY - Speech to Text")
            show_ready_banner()
            return

        # Show processing status
        set_console_title("⏳ PROCESSING - Speech to Text")
        show_processing_banner()

        # Restore volume before processing (so user can hear feedback)
        if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE and original_volume is not None:
            set_volume(original_volume)

        try:
            # Recognize speech
            text = recognizer.recognize_google(audio, language=LANGUAGE)

            # Success beep
            beep(1200, 100)
            time.sleep(0.1)
            beep(1200, 100)

            # Type the text
            type_text(text)

            # Show result temporarily
            print(f"\n  ✅ Typed: {text}\n")
            time.sleep(2)

        except sr.WaitTimeoutError:
            beep(400, 200)  # Low beep for error
            print("\n  ⏱️ No speech detected (timeout)\n")
            time.sleep(2)
        except sr.UnknownValueError:
            beep(400, 200)
            print("\n  ❌ Could not understand audio\n")
            time.sleep(2)
        except sr.RequestError as e:
            beep(400, 200)
            print(f"\n  ❌ Could not request results; {e}\n")
            time.sleep(2)
        except Exception as e:
            beep(400, 200)
            print(f"\n  ❌ Error: {e}\n")
            time.sleep(2)

    except Exception as e:
        beep(400, 200)
        print(f"\n  ❌ Unexpected error: {e}\n")
        time.sleep(2)
    finally:
        # Restore volume if not already restored
        if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE and original_volume is not None:
            set_volume(original_volume)

        is_recording = False
        set_console_title("✅ READY - Speech to Text")
        show_ready_banner()

def toggle_recording():
    """Toggle recording on/off"""
    global is_recording, recording_thread

    if not is_recording:
        is_recording = True
        recording_thread = threading.Thread(target=record_and_transcribe, daemon=True)
        recording_thread.start()
    else:
        is_recording = False
        beep(800, 150)  # Stop beep
        set_console_title("✅ READY - Speech to Text")

def main():
    """Main function"""
    set_console_title("✅ READY - Speech to Text")
    show_ready_banner()

    # Check if volume control is available
    if AUTO_DUCK_VOLUME and not VOLUME_CONTROL_AVAILABLE:
        print("  ⚠️ Warning: pycaw not installed. Volume ducking disabled.")
        print("  Install with: pip install pycaw comtypes")
        print("\n")
        time.sleep(3)

    # Register the hotkey
    keyboard.add_hotkey(HOTKEY, toggle_recording)

    try:
        # Keep the program running
        keyboard.wait()
    except KeyboardInterrupt:
        set_console_title("Speech to Text - Exiting")
        print("\n\n  👋 Exiting...\n")

if __name__ == "__main__":
    main()
