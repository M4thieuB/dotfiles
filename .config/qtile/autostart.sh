#!/bin/sh

# Launch picom
picom --experimental-backends &

numlockx on 

# Launch the notification server
dunst -conf ~/.config/dunst/dunstrc &

# Launch nitrogen
nitrogen --restore &
