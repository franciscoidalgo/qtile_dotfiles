from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from libqtile.lazy import lazy
from modules.keys import terminal
import os

from modules.palettes import catppuccin

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text=" 異", mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")}, background=catppuccin["pink"], foreground=catppuccin["surface0"]),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["pink"],
                    background=catppuccin["red"],
                ),
                widget.CurrentLayoutIcon(
                    padding=1,
                    scale=0.8,
                    background=catppuccin["red"],
                    custom_icon_paths=[os.path.expanduser(
                        "~/.config/qtile/icons/")],
                ),
                widget.CurrentLayout(
                    background=catppuccin["red"], foreground=catppuccin["crust"]),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["red"],
                    background=catppuccin["peach"],
                ),
                widget.GroupBox(
                    highlight_method='line',
                    background=catppuccin["peach"],
                    highlight_color=[catppuccin["peach"], catppuccin["peach"]],
                    other_screen_border=catppuccin["overlay1"],
                    other_current_screen_border=catppuccin["text"],
                    this_current_screen_border=catppuccin["text"],
                    this_screen_border=catppuccin["overlay1"],
                    inactive=catppuccin["surface0"],
                ),
                widget.TextBox(
                    text="", padding=0, fontsize=30, foreground=catppuccin["peach"]
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(fontsize=12, foreground='#99c0de', fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CheckUpdates(
                    no_update_string="",
                    update_interval=300,
                    distro="Arch_yay",
                    display_format="{updates} ",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                ),
                widget.Systray(icon_size=20),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["blue"]
                ),
                widget.Volume(
                    fmt="墳 {}",
                    mute_command="amixer -D pulse set Master toggle",
                    background=catppuccin["blue"],
                    foreground=catppuccin["crust"]
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["teal"],
                    background=catppuccin["blue"],
                ),
                widget.CPU(
                    format=" {load_percent:04}%",
                    mouse_callbacks={"Button1": lazy.spawn(
                        terminal + " -e btop")},
                    foreground=catppuccin["crust"],
                    background=catppuccin["teal"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["green"],
                    background=catppuccin["teal"],
                ),
                widget.Memory(
                    fmt="{}",
                    mouse_callbacks={"Button1": lazy.spawn(
                        terminal + " -e btop")},
                    foreground=catppuccin["crust"],
                    background=catppuccin["green"],
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["yellow"],
                    background=catppuccin["green"],
                ),
                widget.CapsNumLockIndicator(
                    foreground=catppuccin["crust"],
                    fmt=" {}",
                    background=catppuccin["yellow"]
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["peach"],
                    background=catppuccin["yellow"],
                ),
                widget.Clock(format=" %a %d %b %Y, %I:%M %p",
                             background=catppuccin["peach"], foreground=catppuccin["crust"]),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=30,
                    foreground=catppuccin["red"],
                    background=catppuccin["peach"],
                ),
                widget.TextBox(
                    text="  ",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser(
                            '~/.config/rofi/powermenu.sh')),
                    },
                    background=catppuccin["red"],
                    foreground=catppuccin["crust"],
                ),
            ],
            24,  # height in px
            background=catppuccin["base"],  # background color
        ), ),
]
