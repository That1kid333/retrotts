"""
Quick script to create all theme variants
"""

import shutil

# Read the base retro file
with open('system_speech_retro.py', 'r', encoding='utf-8') as f:
    base_code = f.read()

# Theme configurations
themes = {
    'vaporwave': {
        'name': 'VAPORWAVE',
        'description': 'A E S T H E T I C - Pink & Cyan Dreams',
        'colors': {
            'neon_cyan': 'bright_cyan',
            'neon_magenta': 'bright_magenta',
            'neon_green': 'bright_magenta',
            'neon_yellow': 'bright_cyan',
            'neon_red': 'bright_magenta',
            'dim': 'cyan',
            'bg': 'black'
        }
    },
    'amber': {
        'name': 'AMBER TERMINAL',
        'description': 'Classic Unix Terminal - Vintage Computing',
        'colors': {
            'neon_cyan': 'yellow',
            'neon_magenta': 'bright_yellow',
            'neon_green': 'yellow',
            'neon_yellow': 'bright_yellow',
            'neon_red': 'bright_yellow',
            'dim': 'dim yellow',
            'bg': 'black'
        }
    },
    'neon': {
        'name': 'NEON CITY',
        'description': 'Bright Lights, Big City - Rainbow Overload',
        'colors': {
            'neon_cyan': 'bright_cyan',
            'neon_magenta': 'bright_magenta',
            'neon_green': 'bright_green',
            'neon_yellow': 'bright_yellow',
            'neon_red': 'bright_red',
            'dim': 'bright_white',
            'bg': 'black'
        }
    },
    'midnight': {
        'name': 'MIDNIGHT BLUE',
        'description': 'Cool Professional - Azure Dreams',
        'colors': {
            'neon_cyan': 'bright_cyan',
            'neon_magenta': 'bright_blue',
            'neon_green': 'cyan',
            'neon_yellow': 'bright_cyan',
            'neon_red': 'bright_blue',
            'dim': 'dim cyan',
            'bg': 'black'
        }
    }
}

for theme_key, theme_config in themes.items():
    print(f"Creating {theme_config['name']} theme...")

    # Create the theme file
    theme_code = base_code

    # Update the description
    theme_code = theme_code.replace(
        'Retro-Cyberpunk Speech to Text Terminal',
        f"{theme_config['name']} THEME - {theme_config['description']}"
    )

    # Update the colors
    original_colors = """# Retro color scheme
COLORS = {
    'neon_cyan': 'bright_cyan',
    'neon_magenta': 'bright_magenta',
    'neon_green': 'bright_green',
    'neon_yellow': 'bright_yellow',
    'neon_red': 'bright_red',
    'dim': 'dim white',
    'bg': 'black'
}"""

    new_colors = f"""# {theme_config['name']} color scheme
COLORS = {{
    'neon_cyan': '{theme_config['colors']['neon_cyan']}',
    'neon_magenta': '{theme_config['colors']['neon_magenta']}',
    'neon_green': '{theme_config['colors']['neon_green']}',
    'neon_yellow': '{theme_config['colors']['neon_yellow']}',
    'neon_red': '{theme_config['colors']['neon_red']}',
    'dim': '{theme_config['colors']['dim']}',
    'bg': '{theme_config['colors']['bg']}'
}}"""

    theme_code = theme_code.replace(original_colors, new_colors)

    # Write the theme file
    filename = f'system_speech_{theme_key}.py'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(theme_code)

    print(f"[OK] Created {filename}")

print("\n✨ All themes created successfully!")
print("\nThemes available:")
print("1. system_speech_retro.py - Original Cyberpunk")
print("2. system_speech_matrix.py - Matrix Green")
print("3. system_speech_vaporwave.py - Vaporwave Pink/Cyan")
print("4. system_speech_amber.py - Amber Terminal")
print("5. system_speech_neon.py - Neon City Rainbow")
print("6. system_speech_midnight.py - Midnight Blue")
