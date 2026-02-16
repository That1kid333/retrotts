"""
Beautiful Theme Selector for Retro TTS
"""

import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich import box
import time

console = Console()

THEMES = {
    '1': {
        'name': 'CYBERPUNK',
        'desc': 'Original - Neon Dreams',
        'colors': 'Cyan/Magenta/Green',
        'vibe': 'Retro-Futuristic',
        'file': 'run_retro.bat',
        'color': 'bright_cyan'
    },
    '2': {
        'name': 'MATRIX',
        'desc': 'The Hacker - Code Rain',
        'colors': 'All Green',
        'vibe': 'Terminal Purist',
        'file': 'run_matrix.bat',
        'color': 'bright_green'
    },
    '3': {
        'name': 'VAPORWAVE',
        'desc': 'A E S T H E T I C',
        'colors': 'Pink & Cyan',
        'vibe': '80s/90s Retro',
        'file': 'run_vaporwave.bat',
        'color': 'bright_magenta'
    },
    '4': {
        'name': 'AMBER TERMINAL',
        'desc': 'Vintage Computing',
        'colors': 'Classic Amber',
        'vibe': 'Unix Nostalgia',
        'file': 'run_amber.bat',
        'color': 'bright_yellow'
    },
    '5': {
        'name': 'NEON CITY',
        'desc': 'Rainbow Overload',
        'colors': 'ALL Colors',
        'vibe': 'Maximum Impact',
        'file': 'run_neon.bat',
        'color': 'bright_white'
    },
    '6': {
        'name': 'MIDNIGHT BLUE',
        'desc': 'Cool Professional',
        'colors': 'Azure Blues',
        'vibe': 'Corporate Cyber',
        'file': 'run_midnight.bat',
        'color': 'bright_blue'
    }
}

def create_header():
    """Create the awesome header"""
    header_text = """
╔═══════════════════════════════════════════════════════════════════════╗
║  ████████╗██╗  ██╗███████╗███╗   ███╗███████╗                        ║
║  ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝                        ║
║     ██║   ███████║█████╗  ██╔████╔██║█████╗                          ║
║     ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝                          ║
║     ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗                        ║
║     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝                        ║
║                                                                       ║
║  ███████╗███████╗██╗     ███████╗ ██████╗████████╗ ██████╗ ██████╗  ║
║  ██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗ ║
║  ███████╗█████╗  ██║     █████╗  ██║        ██║   ██║   ██║██████╔╝ ║
║  ╚════██║██╔══╝  ██║     ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗ ║
║  ███████║███████╗███████╗███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║ ║
║  ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ║
╚═══════════════════════════════════════════════════════════════════════╝
    """

    header = Text()
    lines = header_text.split('\n')
    colors = ['bright_cyan', 'bright_magenta', 'bright_green', 'bright_yellow', 'bright_cyan', 'bright_magenta']

    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        header.append(line + '\n', style=color)

    return Panel(
        Align.center(header),
        style="bright_magenta on black",
        box=box.DOUBLE,
        padding=(0, 2)
    )

def create_theme_card(key, theme):
    """Create a beautiful theme card"""
    card = Table.grid(padding=(0, 2))
    card.add_column(justify="right", style="dim")
    card.add_column(justify="left")

    # Theme name with color
    name_text = Text(theme['name'], style=f"{theme['color']} bold")
    card.add_row(f"[{key}]", name_text)
    card.add_row("", Text(theme['desc'], style="dim"))
    card.add_row("Colors:", Text(theme['colors'], style=theme['color']))
    card.add_row("Vibe:", Text(theme['vibe'], style="bright_white"))

    return Panel(
        card,
        border_style=theme['color'],
        box=box.HEAVY,
        padding=(0, 1)
    )

def show_menu():
    """Display the theme selection menu"""
    console.clear()

    # Header
    console.print(create_header())
    console.print()

    # Subtitle
    subtitle = Text("Choose Your Aesthetic", style="bright_yellow bold")
    console.print(Align.center(subtitle))
    console.print()

    # Theme cards in a grid layout
    table = Table.grid(padding=1)
    table.add_column()
    table.add_column()

    # Add themes in 2x3 grid
    for i in range(0, 6, 2):
        key1 = str(i + 1)
        key2 = str(i + 2)
        table.add_row(
            create_theme_card(key1, THEMES[key1]),
            create_theme_card(key2, THEMES[key2])
        )

    console.print(Align.center(table))
    console.print()

    # Instructions
    instructions = Panel(
        Text.assemble(
            ("Press ", "dim"),
            ("1-6", "bright_cyan bold"),
            (" to select a theme • Press ", "dim"),
            ("0", "bright_red bold"),
            (" to exit", "dim")
        ),
        border_style="bright_green",
        box=box.ROUNDED
    )
    console.print(Align.center(instructions))
    console.print()

def launch_theme(theme_file):
    """Launch the selected theme"""
    console.print()
    console.print(
        Panel(
            Text("🚀 Launching theme...", style="bright_green bold", justify="center"),
            border_style="bright_green"
        )
    )
    time.sleep(0.5)

    # Launch the batch file
    try:
        # Use start command to launch in new window
        subprocess.Popen(['cmd', '/c', 'start', theme_file], shell=True)
        console.print(
            Text("✓ Theme launched! Closing selector...", style="bright_cyan", justify="center")
        )
        time.sleep(1)
    except Exception as e:
        console.print(f"[bright_red]Error launching theme: {e}[/]")
        time.sleep(2)

def main():
    """Main function"""
    while True:
        show_menu()

        # Get user choice
        try:
            choice = console.input("[bright_yellow]→ Enter your choice: [/]").strip()

            if choice == '0':
                console.print()
                console.print(
                    Text("👋 Goodbye!", style="bright_magenta bold", justify="center")
                )
                time.sleep(0.5)
                break

            if choice in THEMES:
                theme = THEMES[choice]
                launch_theme(theme['file'])
                break
            else:
                console.print()
                console.print(
                    Panel(
                        Text("❌ Invalid choice! Please enter 1-6 or 0 to exit",
                             style="bright_red bold",
                             justify="center"),
                        border_style="bright_red"
                    )
                )
                time.sleep(1.5)
        except KeyboardInterrupt:
            console.print()
            console.print(
                Text("👋 Goodbye!", style="bright_magenta bold", justify="center")
            )
            break

if __name__ == "__main__":
    main()
