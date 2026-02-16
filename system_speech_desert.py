"""
██████╗ ██████╗ ██╗███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗
██╔══██╗██╔══██╗██║████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║██╔══██╗██║
██████╔╝██████╔╝██║██╔████╔██║██║   ██║██████╔╝██║  ██║██║███████║██║
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██║   ██║██╔══██╗██║  ██║██║██╔══██║██║
██║     ██║  ██║██║██║ ╚═╝ ██║╚██████╔╝██║  ██║██████╔╝██║██║  ██║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚══════╝

🌌 PrehiTech - Ancient × Ancient - Prehistoric Cyberpunk TTS 🦕⚡
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
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich import box
from rich.progress import BarColumn, Progress
import random

# Fix Windows console encoding (only if console exists)
if sys.stdout is not None and hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr is not None and hasattr(sys.stderr, 'buffer'):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Initialize
console = Console()
recognizer = sr.Recognizer()
keyboard_controller = Controller()
is_recording = False
recording_thread = None
original_volume = None
current_audio_level = 0.0
transcribed_text = ""

# Configuration
HOTKEY = 'ctrl+shift+space'
LANGUAGE = 'en-US'
AUTO_DUCK_VOLUME = True
DUCK_PERCENTAGE = 0.3
SILENCE_PAUSE = 3.0
MAX_RECORDING_TIME = 120

# Desert Sunset color scheme - Sahara Dusk
COLORS = {
    'neon_cyan': 'bright_yellow',      # Sand glow
    'neon_magenta': 'magenta',         # Sunset purple
    'neon_green': 'yellow',            # Desert heat
    'neon_yellow': 'red',              # Coral sunset
    'neon_red': 'bright_red',          # Horizon fire
    'dim': 'dim yellow',               # Sand dunes
    'bg': 'black'                      # Desert night
}

# Try to import volume control
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
    """Get current system volume"""
    volume_interface = get_volume_interface()
    if volume_interface:
        try:
            return volume_interface.GetMasterVolumeLevelScalar()
        except:
            pass
    return None

def set_volume(level):
    """Set system volume"""
    volume_interface = get_volume_interface()
    if volume_interface:
        try:
            volume_interface.SetMasterVolumeLevelScalar(level, None)
            return True
        except:
            pass
    return False

def create_retro_vu_meter(level, width=60):
    """Create a retro-style VU meter"""
    filled = int(width * level)

    # Different characters for different intensity levels
    if level < 0.3:
        char = '░'
        color = COLORS['neon_green']
    elif level < 0.7:
        char = '▒'
        color = COLORS['neon_cyan']
    else:
        char = '█'
        color = COLORS['neon_magenta']

    bar = char * filled + '·' * (width - filled)

    # Create the meter with brackets
    meter = Text()
    meter.append("┤", style=COLORS['dim'])
    meter.append(bar, style=color)
    meter.append("├", style=COLORS['dim'])

    return meter

def create_glitch_text(text, intensity=0.1):
    """Add glitch effect to text"""
    glitch_chars = ['▓', '▒', '░', '█', '▄', '▀', '▌', '▐']
    result = Text()

    for char in text:
        if random.random() < intensity:
            result.append(random.choice(glitch_chars), style=COLORS['neon_cyan'])
        else:
            result.append(char)

    return result

def create_header():
    """Create the retro header"""
    header_art = """
╔═══════════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗████████╗██████╗  ██████╗     ████████╗████████╗███████╗ ║
║  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝╚══██╔══╝██╔════╝ ║
║  ██████╔╝█████╗     ██║   ██████╔╝██║   ██║       ██║      ██║   ███████╗ ║
║  ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║       ██║      ██║   ╚════██║ ║
║  ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝       ██║      ██║   ███████║ ║
║  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝      ╚═╝   ╚══════╝ ║
╚═══════════════════════════════════════════════════════════════════════╝
    """

    header = Text()
    for line in header_art.split('\n'):
        header.append(line + '\n', style=COLORS['neon_cyan'])

    return Panel(
        Align.center(header),
        style=f"{COLORS['neon_magenta']} on {COLORS['bg']}",
        box=box.DOUBLE
    )

def create_status_panel(status, level=0.0):
    """Create status display panel"""
    table = Table.grid(padding=(0, 2))
    table.add_column(justify="right", style=COLORS['dim'])
    table.add_column(justify="left")

    # Status indicator
    if status == "READY":
        indicator = Text("● READY", style=COLORS['neon_green'] + " bold")
        status_text = "Press Ctrl+Shift+Space to begin"
    elif status == "RECORDING":
        indicator = Text("● REC", style=COLORS['neon_red'] + " bold blink")
        status_text = "Stop talking for 3s to finish"
    elif status == "PROCESSING":
        indicator = Text("◐ PROCESSING", style=COLORS['neon_yellow'] + " bold")
        status_text = "Converting speech to text..."
    else:
        indicator = Text("○ IDLE", style=COLORS['dim'])
        status_text = ""

    table.add_row("STATUS:", indicator)
    table.add_row("HOTKEY:", Text("Ctrl+Shift+Space", style=COLORS['neon_cyan']))
    table.add_row("LANGUAGE:", Text(LANGUAGE, style=COLORS['neon_green']))
    table.add_row("SILENCE:", Text(f"{SILENCE_PAUSE}s", style=COLORS['neon_green']))
    table.add_row("MAX TIME:", Text(f"{MAX_RECORDING_TIME}s", style=COLORS['neon_green']))

    if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE:
        table.add_row("DUCKING:", Text(f"{int(DUCK_PERCENTAGE*100)}%", style=COLORS['neon_magenta']))

    table.add_row("", Text(""))
    table.add_row("INFO:", Text(status_text, style=COLORS['dim']))

    return Panel(
        table,
        title="[" + COLORS['neon_cyan'] + "]⚡ SYSTEM STATUS ⚡[/]",
        border_style=COLORS['neon_cyan'],
        box=box.HEAVY
    )

def create_vu_panel(level):
    """Create VU meter panel"""
    meter = create_retro_vu_meter(level, width=60)

    # Percentage display
    percent = Text(f"{int(level * 100):3d}%", style=COLORS['neon_yellow'] + " bold")

    # Level indicator
    if level < 0.3:
        level_text = Text("TOO QUIET", style=COLORS['dim'])
    elif level < 0.7:
        level_text = Text("OPTIMAL", style=COLORS['neon_green'] + " bold")
    else:
        level_text = Text("LOUD", style=COLORS['neon_magenta'] + " bold")

    content = Table.grid(padding=(0, 1))
    content.add_column(justify="left")
    content.add_row(meter)
    content.add_row("")
    content.add_row(Text.assemble(("LEVEL: ", COLORS['dim']), percent, ("  ", ""), level_text))

    return Panel(
        Align.center(content),
        title="[" + COLORS['neon_magenta'] + "]▬▬▬ AUDIO INPUT ▬▬▬[/]",
        border_style=COLORS['neon_magenta'],
        box=box.HEAVY
    )

def create_output_panel(text):
    """Create output text panel"""
    if text:
        display_text = Text(text, style=COLORS['neon_cyan'] + " bold")
    else:
        display_text = Text("[ Awaiting input... ]", style=COLORS['dim'] + " italic")

    return Panel(
        Align.left(display_text),
        title="[" + COLORS['neon_green'] + "]✎ TRANSCRIBED OUTPUT ✎[/]",
        border_style=COLORS['neon_green'],
        box=box.HEAVY,
        padding=(1, 2)
    )

def create_layout(status="READY", level=0.0, output_text=""):
    """Create the main layout"""
    layout = Layout()

    layout.split_column(
        Layout(create_header(), size=11),
        Layout(name="main", ratio=1)
    )

    layout["main"].split_row(
        Layout(create_status_panel(status, level), ratio=1),
        Layout(name="right", ratio=2)
    )

    layout["main"]["right"].split_column(
        Layout(create_vu_panel(level), size=7),
        Layout(create_output_panel(output_text), ratio=1)
    )

    return layout

def type_text(text):
    """Type the text into the active window"""
    time.sleep(0.1)
    for char in text:
        keyboard_controller.type(char)
    keyboard_controller.type(' ')

def get_rms(data):
    """Calculate RMS of audio data"""
    try:
        count = len(data) / 2
        format = "%dh" % (count)
        shorts = struct.unpack(format, data)
        sum_squares = sum([sample ** 2 for sample in shorts])
        rms = math.sqrt(sum_squares / count)
        return rms
    except:
        return 0

def record_with_visualization(live):
    """Record audio with real-time visualization"""
    global current_audio_level

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    SILENCE_THRESHOLD = 300
    SILENCE_DURATION = SILENCE_PAUSE
    MAX_DURATION = MAX_RECORDING_TIME

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

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
            current_audio_level = min(1.0, rms / 3000)

            # Update display
            live.update(create_layout("RECORDING", current_audio_level, transcribed_text))

            # Detect speech
            if rms > SILENCE_THRESHOLD:
                started_speaking = True
                silent_chunks = 0
            elif started_speaking:
                silent_chunks += 1
                if silent_chunks > silence_chunks_needed:
                    break

    except Exception as e:
        console.print(f"[{COLORS['neon_red']}]Error recording: {e}[/]")
        return None
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    # Convert to audio data
    audio_data = b''.join(frames)
    audio = sr.AudioData(audio_data, RATE, 2)
    return audio

def record_and_transcribe(live):
    """Record audio and transcribe to text"""
    global is_recording, original_volume, current_audio_level, transcribed_text

    set_console_title("🔴 RECORDING - Retro TTS")
    beep(1000, 150)

    # Lower volume if enabled
    if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE:
        original_volume = get_current_volume()
        if original_volume is not None:
            set_volume(original_volume * DUCK_PERCENTAGE)

    try:
        # Record audio with visualization
        audio = record_with_visualization(live)

        if audio is None:
            is_recording = False
            set_console_title("✅ READY - Retro TTS")
            return

        # Show processing status
        set_console_title("⏳ PROCESSING - Retro TTS")
        live.update(create_layout("PROCESSING", 0.0, transcribed_text))

        # Restore volume
        if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE and original_volume is not None:
            set_volume(original_volume)

        try:
            # Recognize speech
            text = recognizer.recognize_google(audio, language=LANGUAGE)

            # Success beep
            beep(1200, 100)
            time.sleep(0.1)
            beep(1200, 100)

            # Update transcribed text
            transcribed_text = text
            live.update(create_layout("READY", 0.0, transcribed_text))

            # Type the text
            type_text(text)

            time.sleep(2)

        except sr.UnknownValueError:
            beep(400, 200)
            transcribed_text = "[ERROR] Could not understand audio"
            live.update(create_layout("READY", 0.0, transcribed_text))
            time.sleep(2)
        except sr.RequestError as e:
            beep(400, 200)
            transcribed_text = f"[ERROR] {e}"
            live.update(create_layout("READY", 0.0, transcribed_text))
            time.sleep(2)
        except Exception as e:
            beep(400, 200)
            transcribed_text = f"[ERROR] {e}"
            live.update(create_layout("READY", 0.0, transcribed_text))
            time.sleep(2)

    except Exception as e:
        beep(400, 200)
        console.print(f"[{COLORS['neon_red']}]Unexpected error: {e}[/]")
    finally:
        # Restore volume
        if AUTO_DUCK_VOLUME and VOLUME_CONTROL_AVAILABLE and original_volume is not None:
            set_volume(original_volume)

        is_recording = False
        current_audio_level = 0.0
        set_console_title("✅ READY - Retro TTS")
        live.update(create_layout("READY", 0.0, transcribed_text))

def toggle_recording(live):
    """Toggle recording on/off"""
    global is_recording, recording_thread

    if not is_recording:
        is_recording = True
        recording_thread = threading.Thread(target=record_and_transcribe, args=(live,), daemon=True)
        recording_thread.start()
    else:
        is_recording = False
        beep(800, 150)

def main():
    """Main function"""
    console.clear()
    set_console_title("✅ READY - Retro TTS")

    with Live(create_layout("READY", 0.0, ""), refresh_per_second=10, screen=True, transient=False) as live:
        # Register hotkey
        keyboard.add_hotkey(HOTKEY, lambda: toggle_recording(live))

        try:
            # Keep running
            while True:
                try:
                    live.update(create_layout(
                        "RECORDING" if is_recording else "READY",
                        current_audio_level,
                        transcribed_text
                    ))
                except Exception:
                    # If Live display gets interrupted (e.g., by clicking), just continue
                    pass
                time.sleep(0.1)
        except KeyboardInterrupt:
            console.print(f"\n[{COLORS['neon_cyan']}]Exiting Retro TTS...[/]")

if __name__ == "__main__":
    main()
