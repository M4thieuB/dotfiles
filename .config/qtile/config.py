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

from typing import List  # noqa: F401
import os
import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile import qtile

mod = "mod4"


colors = [  "#2e3440", # Background         1
            "#f34a00", # Orange             2
            "#b2c8d6", # Bleu moins clair   3
            "#ff355b", # Rouge Rose         4
            "#b6e875", # Vert clair         5
            "#ffc150", # Jaune/Orange       6
            "#75d3ff", # Bleu un peu pétard 7
            "#b975e6", # Violet             8
            "#6cbeb5", # Cyan               9
            "#c1c8d6"] # Bleu/Gris          10


dmenu_param = dict(
    dmenu_font = "Fira Code Medium",
    dmenu_prompt=">",
    background = colors[0],
    foreground= colors[6],
    selected_background=colors[5],
    selected_foreground=colors[0]
)


### Start applications at start ###
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


keys = [

    ############### CHORDS ###############
    KeyChord(   [mod], "v", [
                # More precise sound management
                Key([], "a", lazy.spawn("amixer -q sset Master 1%-")),
                Key([], "e", lazy.spawn("amixer -q sset Master 1%+"))],
                mode=" Volume"
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
                mode="Resize"

    ),


    # Mute sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle")),

    # More precise sound management
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+")),


    # Change the focus
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),

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
        lazy.spawn("kitty"),
        desc="Launch terminal"
        ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Toggle fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),



    # Open dmenu
    Key([mod], 'd', lazy.run_extension(extension.DmenuRun(**dmenu_param))),

    # Manage my screen's brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5")),
    ]



groups = []

# FOR QWERTY KEYBOARDS
# group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "minus", "egrave", "underscore", "ccedilla", "agrave",]

group_labels = ["", "", "", "", "", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

group_class = ["firefox", "Atom","","discord","","","","","",""]

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


def layout_defaults():
    return dict(
        border_focus=colors[5],
        border_normal=colors[0],
        border_width=2,
        margin = 6
        )

layout_theme = layout_defaults()

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
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

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                        borderwidth=2,
                        active = colors[5],
                        inactive = colors[5],
                        hide_unused = True,
                        foreground = colors[5],
                        background = colors[0],
                        block_highlight_text_color = colors[5],
                        spacing = 2,
                        highlight_method = 'block',
                        rounded = True,
                        margin_x = 5,
                        margin_y = 3,
                        padding_x = 10,
                        padding_y = 5,
                        font = "Font Awesome",
                        fontsize = 15
                        ),

                widget.CurrentLayoutIcon(
                        fmt='{}',
                        background=colors[0],
                        foreground=colors[2],
                        font="Fira Code Medium",
                        fontsize=13,
                        padding=5,
                        scale = 0.6
                        ),

                widget.WindowName(
                        background=colors[0],
                        foreground = colors[6],
                        font="Fira Code Bold",
                        fontsize=15,
                        padding = 10
                        ),

                widget.Chord(
                        background = colors[0],
                        foreground = colors[9],
                        fmt = '{}',
                        fontsize = 15,
                        font = "Fira Code Medium",
                        padding = 5
                        ),

                widget.TextBox(
                        text='/',
                        foreground=colors[3],
                        background=colors[0],
                        padding=0,
                        font="Fira Code Bold",
                        fontsize=37
                        ),

                widget.Net(
                        font="Fira Code Medium",
                        fontsize=15,
                        interface="wlp1s0",
                        format = '{down} ↓↑ {up}',
                        foreground=colors[7],
                        background=colors[0],
                        padding=5
                        ),

                # widget.Sep(
                #         background=colors[0],
                #         foreground='aaaaaa',
                #         linewidth=3,
                #         padding=5,
                #         size_percent=60
                # ),
                widget.TextBox(
                        text='/',
                        foreground=colors[3],
                        background=colors[0],
                        padding=0,
                        font="Fira Code Bold",
                        fontsize=37
                        ),

                widget.Volume(
                        background=colors[0],
                        foreground=colors[4],
                        font="Font Awesome",
                        fontsize=15,
                        fmt = '  {}',
                        get_volume_command=None,
                        padding = 5,
                        ),

                widget.TextBox(
                        text='/',
                        foreground=colors[3],
                        background=colors[0],
                        padding=0,
                        font="Fira Code Bold",
                        fontsize=37
                        ),

                # widget.CPU(
                #         background=colors[0],
                #         foreground=colors[5],
                #         font="Font Awesome",
                #         fontsize=15,
                #         format='  {load_percent}%',
                #         padding = 5,
                #         ),
                widget.TextBox(
                        fmt = "",
                        font = 'Font Awesome',
                        fontsize = 30,
                        background=colors[0],
                        foreground=colors[2],
                        # mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("dm-wifi \
                        #     -p '{0}' -fn '{1}' -nb '{2}' -nf '{3}' -sb '{4}' -sf '{5}'".format(
                        #     dmenu_param["dmenu_prompt"],
                        #     dmenu_param["dmenu_font"],
                        #     dmenu_param["background"],
                        #     dmenu_param["foreground"],
                        #     dmenu_param["selected_background"],
                        #     dmenu_param["selected_foreground"])
                        #     )},
                        margin=5
                ),

                # widget.TextBox(
                #         text='/',
                #         foreground=colors[3],
                #         background=colors[0],
                #         padding=0,
                #         font="Fira Code Bold",
                #         fontsize=37
                #         ),

                widget.Battery(
                        background=colors[0],
                        foreground=colors[2],
                        font="Fira Code Medium",
                        fontsize=15,
                        battery=0,                 # Which battery should be monitored (battery number or name)
                        charge_char='',           # Character to indicate the battery is charging
                        discharge_char='',        # Character to indicate the battery is discharging
                        empty_char='',
                        format = '{char} {percent:2.0%}', # add {hour:d}:{min:02d} for time
                        padding=5
                        ),

                widget.TextBox(
                        text='/',
                        foreground=colors[3],
                        background=colors[0],
                        padding=0,
                        font="Fira Code Bold",
                        fontsize=37
                        ),

                widget.TextBox(
                        text=' ',
                        foreground=colors[6],
                        background=colors[0],
                        padding=0,
                        font="Font Awesome",
                        fontsize=15
                        ),

                widget.Clock(
                        font="Fira Code Medium",
                        fontsize=15,
                        format="%H:%M   %A %d %B",
                        background=colors[0],
                        foreground=colors[6],
                        padding = 5
                        ),

                widget.Image(
                        filename='~/.config/qtile/icon/archicon.png',
                        background=colors[0],
                        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("dm-logout \
                            -p '{0}' -fn '{1}' -nb '{2}' -nf '{3}' -sb '{4}' -sf '{5}'".format(
                            dmenu_param["dmenu_prompt"],
                            dmenu_param["dmenu_font"],
                            dmenu_param["background"],
                            dmenu_param["foreground"],
                            dmenu_param["selected_background"],
                            dmenu_param["selected_foreground"])
                            )},
                        margin=5
                )

            ],
            30,
            opacity = 0.8,
            margin = 8,
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
