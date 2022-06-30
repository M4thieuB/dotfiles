#!/bin/bash

# Terminate already running bar instances
killall -q polybar
# If all your bars have ipc enabled, you can also use 
# polybar-msg cmd quit

# Launch Polybar, using default config location ~/.config/polybar/config.ini
# polybar example 2>&1 | tee -a /tmp/polybar.log & disown

while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

## Launch
# my_laptop_external_monitor=$(xrandr --query | grep 'DP-1-0.8')
# if [[ $my_laptop_external_monitor = DP-1-0.8\ connected* ]]; then
# else
# fi

polybar left -c ~/.config/polybar/config.ini &
sleep 1 &&
polybar center -c ~/.config/polybar/config.ini &
# polybar music -c ~/.config/polybar/config.ini &
polybar right -c ~/.config/polybar/config.ini &
polybar right-lvds -c ~/.config/polybar/config.ini &
