#!/bin/sh

# Launch picom
picom --experimental-backends &

numlockx on 

# Launch the notification server
dunst -conf ~/.config/dunst/dunstrc &

# Launch nitrogen
nitrogen --restore &

# Launch nm-applet for managing wifi connections easily in the systray widget of qtile
nm-applet &

# Launch the emacs daemon (server/client application)
/usr/bin/emacs --daemon
