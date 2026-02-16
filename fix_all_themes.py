"""
Apply the clicking fix to all theme files
"""

theme_files = [
    'system_speech_matrix.py',
    'system_speech_vaporwave.py',
    'system_speech_amber.py',
    'system_speech_neon.py',
    'system_speech_midnight.py'
]

# The old code that needs to be replaced
old_code = """    with Live(create_layout("READY", 0.0, ""), refresh_per_second=10, screen=True) as live:
        # Register hotkey
        keyboard.add_hotkey(HOTKEY, lambda: toggle_recording(live))

        try:
            # Keep running
            while True:
                live.update(create_layout(
                    "RECORDING" if is_recording else "READY",
                    current_audio_level,
                    transcribed_text
                ))
                time.sleep(0.1)
        except KeyboardInterrupt:
            console.print(f"\\n[{COLORS['neon_cyan']}]Exiting Retro TTS...[/]")"""

# The new fixed code
new_code = """    with Live(create_layout("READY", 0.0, ""), refresh_per_second=10, screen=True, transient=False) as live:
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
            console.print(f"\\n[{COLORS['neon_cyan']}]Exiting Retro TTS...[/]")"""

for theme_file in theme_files:
    try:
        with open(theme_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_code in content:
            content = content.replace(old_code, new_code)
            with open(theme_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Fixed {theme_file}")
        else:
            print(f"[SKIP] {theme_file} - already fixed or different structure")
    except Exception as e:
        print(f"[ERROR] {theme_file}: {e}")

print("\nAll theme files updated with clicking fix!")
