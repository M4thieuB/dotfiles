# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, DropDown, ScratchPad
from libqtile.lazy import lazy
from libqtile import hook
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile import qtile

import os
import subprocess
from themes.dracula import colors
from typing import List  # noqa: F401
# Widget modifié
from mywidget import *

mod = "mod4"
myTerm = "kitty"


# dmenu_param = dict(
#     dmenu_font = "Fira Code Medium-15",
#     dmenu_prompt=">",
#     background = colors[0],
#     foreground= colors[6],
#     selected_background=colors[5],
#     selected_foreground=colors[0],
#     borderwidth=2,
#     number_lines=10
# )


########### Start applications at start ############
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


keys = [




    ############### CHORDS ###############

    KeyChord(   [mod], "v", [
                # More precise sound management
                Key([], "a", lazy.spawn("amixer -q sset Master 1%-")),
                Key([], "e", lazy.spawn("amixer -q sset Master 1%+")),
                Key([], "p", lazy.spawn("pavucontrol"))],
                mode=" Volume"
                ),

    KeyChord(   [mod], "b", [
                # More precise brightness management
                Key([], "a", lazy.spawn("brightnessctl set 5-")),
                Key([], "e", lazy.spawn("brightnessctl set +5"))],
                mode=" Brightness"
                ),

    KeyChord(   [mod], "r", [
                # Resize windows
                Key([],"Right",
                    lazy.layout.grow_right(),
                    lazy.layout.grow(),
                    lazy.layout.increase_ratio(),
                    lazy.layout.delete(),
                    ),

                Key([],"Left",
                    lazy.layout.grow_left(),
                    lazy.layout.shrink(),
                    lazy.layout.decrease_ratio(),
                    lazy.layout.add(),
                    ),

                Key([],"Up",
                    lazy.layout.grow_up(),
                    lazy.layout.grow(),
                    lazy.layout.decrease_nmaster(),
                    ),

                Key([],"Down",
                    lazy.layout.grow_down(),
                    lazy.layout.shrink(),
                    lazy.layout.increase_nmaster(),
                    )],
                mode=" Resize"
                ),

    KeyChord(   [mod], "n", [
                Key([],"s", lazy.spawn("dunstctl set-paused toggle")), # Active/Désactive les notif
        #        Key([],"h", lazy.spawn("dunstctl history")) # Affiche l'historique des notif mais où? Bonne question, à travailler
                ],
            mode=" Notification"
            ),

    KeyChord(   [mod], "e", [
                # Spawn my emacsclient
                Key([], "e", lazy.spawn('emacsclient -c -a "emacs"'), desc="Starting emacs"),
                ],
            mode=" Emacs"
            ),

############## KeyMap ################

    # Mute sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle")),

    # More precise sound management
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+")),


    # Change the focus
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),




    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),

    Key(
        [mod],
        "Return",
        lazy.spawn(myTerm),
        desc="Launch terminal"
        ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.spawn("arcolinux-logout"), desc="Shutdown Qtile"),

    # Toggle fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # Open dmenu
    # Key([mod], 'd', lazy.spawn("dmenu_run -c -nb '{}' -nf '{}' -sb '{}' -sf '{}' -l {} -p '{}' -fn '{}' -bw {}".format(
    #         dmenu_param['background'],
    #         dmenu_param['foreground'],
    #         dmenu_param['selected_background'],
    #         dmenu_param['selected_foreground'],
    #         dmenu_param['number_lines'],
    #         dmenu_param['dmenu_prompt'],
    #         dmenu_param['dmenu_font'],
    #         dmenu_param['borderwidth']
    #     ))),

    # Open Rofi
    Key([mod], 'd', lazy.spawn("rofi -show run")),


    # Manage my screen's brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10")),



    ############ SCRATCHPAD - DROPDOWN #######################
    Key([mod, "control"], "l", lazy.group["sp1"].dropdown_toggle('lang')),

    ]



groups = []

# FOR QWERTY KEYBOARDS
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "minus"] #, "egrave", "underscore", "ccedilla", "agrave" si jamais t'en veux plus

group_labels = ["doc", "dev", "www", "chat", "sys", "mail"]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

group_class = ["", "","firefox","discord","",""]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches = Match(wm_class=[group_class[i]])
        ))




for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

scratch = [
    ScratchPad(
        "sp1",
        [
            # The goal is to drop a little window which displays a translator interface
            DropDown("lang", "kitty python /home/math/Documents/Dev_project/Translator/translate.py", on_focus_lost_hide = False,
                     x = 0.3, y = 0.3, width = 0.4, height = 0.4, opacity = 1),
        ]
    ),
]
groups += scratch


def layout_defaults():
    return dict(
        border_focus=colors[16],
        border_normal=colors[0],
        border_width=2,
        margin = 15
        )

layout_theme = layout_defaults()

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
            **layout_theme
    ),
    layout.MonadWide(
            **layout_theme
    ),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# widget_defaults = dict(
#     font="Fira Code Medium",
#     fontsize=15,
#     padding=5,
# )
# extension_defaults = widget_defaults.copy()

######### Creating Widgets #########
class Dunst(widget.base.ThreadPoolText):
    """
        A simple widget to display the state of the dunst notification server.
        Widget requirements: dunstctl from the dunst package
    """
    defaults = [
        ("update_interval", 1.0, "Update interval for the Dunst widget"),
        (
            "format", "DUNST {state}", "Dunst display format",
        ),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(Dunst.defaults)

    def poll(self):
        variables = dict()

        state = subprocess.check_output(["dunstctl", "is-paused"]).decode("utf-8").strip()
        variables["state"] = "" if state == "false" else ""

        return self.format.format(**variables)


############# Manage what is displayed on screen ##############

screens = [
    Screen(
        top=bar.Bar(
            [
                Dunst(
                        background=colors[0],           # Widget background color
                        fmt="{}",                       # How to format the text
                        font="FiraCode Nerd Font",      # Default font
                        fontsize=15,                    # Font size. Calculated if None.
                        foreground=colors[15],           # Foreground colour
                        format="{state}",               # How to format the text.
                        padding=5,                      # Padding. Calculated if None.
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.GroupBox(
                        borderwidth=2,
                        center_aligned = True,
                        active = colors[4],
                        inactive = colors[3],
                        this_current_screen_border = colors[6],
                        block_highlight_text_color = colors[6],
                        urgent_border = colors[0],
                        urgent_text = colors[7],
                        hide_unused = False,
                        foreground = colors[5],
                        background = colors[0],
                        spacing = 2,
                        highlight_method = 'line',
                        highlight_color = colors[0],
                        rounded = True,
                        margin_x = 5,
                        margin_y = 3,
                        padding_x = 3,
                        padding_y = 5,
                        font = "FiraCode Nerd Font",
                        fontsize = 15
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.CurrentLayout(
                        fmt='{}',
                        background=colors[0],
                        foreground=colors[7],
                        font="Fira Code Medium",
                        fontsize=15,
                        padding=5,
                        scale = 0.6
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.Systray(
                        background = colors[0],
                        padding = 5,
                        icon_size = 20
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.WindowName(
                        background=colors[0],
                        foreground = colors[17],
                        empty_group_string='',
                        format = "{state} {name}",
                        font="Fira Code Medium",
                        fontsize=15,
                        padding = 5
                        ),

                widget.Chord(
                        background = colors[0],
                        foreground = colors[15],
                        fmt = '{}',
                        fontsize = 15,
                        font = "FiraCode Nerd Font Medium",
                        padding = 5
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.CPU(
                    background = colors[0],
                    foreground = colors[13],
                    font = "Fira Code Medium",
                    fontsize = 15,
                    format = " cpu: ({load_percent}%)",
                ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),

                widget.DF(
                    background = colors[0],
                    font = "FiraCode Nerd Font Medium",
                    fontsize = 15,
                    foreground = colors[3],
                    padding = 5,
                    partition = '/',
                    update_interval = 60,
                    format = " {uf} {m}b free", #({r:.03}%)",
                    measure = 'G',
                    max_chars = 30,
                    visible_on_warn = False
                ),

                # MyIPWidget(
                #     background = colors[0],
                #     foreground = colors[5],
                #     font = "Fira Code Medium",
                #     fontsize = 15,
                #     format = "IP (private): {i}",
                #     padding = 5,
                #     interface = "wlp1s0"
                # ),

                widget.TextBox(
                    text = '|',
                    background = colors[0],
                    foreground = colors[10],
                    padding = 5,
                    font = "Fira Code Medium",
                    fontsize = 15
                ),


                widget.GenPollUrl(
                    background = colors[0],
                    foreground = colors[7],
                    font = "Fira Code Medium",
                    fontsize = 15,
                    update_interval = 600,
                    url = "https://api.ipify.org?format=json",
                    parse = lambda x: f"ip: {x['ip']}"
                ),

                # widget.HDDGraph(
                #     background = colors[0],
                #     border_color = colors[4],
                #     border_width = 1,
                #     graph_color = colors[5],
                #     line_width = 2,
                #     margin_x = 3,
                #     margin_y = 3,
                #     path = '/',
                #     type = 'line',
                #     space_type = 'used'
                #     ),

                # widget.Net(
                #         font="Fira Code Medium",
                #         fontsize=15,
                #         interface="wlp1s0",
                #         format = '↓ {down} ↑ {up}',
                #         foreground=colors[7],
                #         background=colors[0],
                #         padding=5
                #         ),

                # widget.Sep(
                #         background=colors[0],
                #         foreground='aaaaaa',
                #         linewidth=3,
                #         padding=5,
                #         size_percent=60
                # ),
                widget.TextBox(
                    text = '|',
                    background = colors[0],
                    foreground = colors[10],
                    padding = 5,
                    font = "Fira Code Medium",
                    fontsize = 15
                    ),


                widget.Volume(
                        background=colors[0],
                        foreground=colors[4],
                        font="FiraCode Nerd Font medium",
                        fontsize=15,
                        fmt = '  {}',
                        get_volume_command=None,
                        padding = 5,
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),


                # widget.CPU(
                #         background=colors[0],
                #         foreground=colors[5],
                #         font="Font Awesome",
                #         fontsize=15,
                #         format='  {load_percent}%',
                #         padding = 5,
                #         ),
                #         ),

                MyBattery(
                        background=colors[0],
                        foreground=colors[5],
                        low_background = colors[0],
                        low_foreground = colors[3],
                        font="FiraCode Nerd Font Medium",
                        fontsize=15,
                        battery=0,                 # Which battery should be monitored (battery number or name)
                        charge_char='',           # Character to indicate the battery is charging
                        discharge_char='',        # Character to indicate the battery is discharging
                        empty_char='',
                        full_char = '',
                        low_percentage = 0.2,
                        notify_below = [20,10,5],      # Niveau auquel on envoie une notif par ordre décroissant
                        format = '{char} {percent:2.0%}', # add {hour:d}:{min:02d} for time
                        padding=5,
                        update_interval = 60,
                        ),

                widget.TextBox(
                        text = '|',
                        background = colors[0],
                        foreground = colors[10],
                        padding = 5,
                        font = "Fira Code Medium",
                        fontsize = 15
                        ),



                widget.TextBox(
                        text=' ',
                        foreground=colors[6],
                        background=colors[0],
                        padding=0,
                        font="FiraCode Nerd Font",
                        fontsize=15
                        ),

                widget.Clock(
                        font="Fira Code Medium",
                        fontsize=15,
                        format="%A %d %B (%H:%M)",
                        background=colors[0],
                        foreground=colors[6],
                        padding = 5
                        ),
            ],
            30,
            opacity = 1,
            margin = 0,
            # border_width=[6, 0, 0, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "#BF363A" , "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
