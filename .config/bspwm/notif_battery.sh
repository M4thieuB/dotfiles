#! /usr/bin/env bash

# Description:  a script to check the state of the battery and throw appropriate notifications.
#   run `sudo systemctl enable cronie` to activate the `cron` daemon if not already done, then
#   add `* * * * * DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=<address> /usr/local/bin/notify_battery.sh level1 level2 ...`
#   to the `cron` table with `crontab -e` and restart the `cron` daemon with
#   `sudo systemctl restart cronie`. The address can be found with `echo $DBUS_SESSION_BUS_ADDRESS`.
# Dependencies: dunst.

help () {
  echo "notif_battery.sh:"
  echo "     a script to check the state of the battery and throw appropriate notifications."
  echo ""
  echo "Usage:" 
  echo "     ./notif_battery.sh level1 level2 level3"
  echo "     In the decreasing order: level1 > level2 > level3"
  echo ""
  echo "Switches: (to do)"
  echo "     -h/--help             shows this help."
  echo "     -p/--print            print the state of the battery in a notification and exit."
  echo "     -c/--check            check the state of the battery and throw a notification if critical."
  echo ""
  exit 0
}

usage () {
  echo "Usage: ./notif_battery.sh level1 level2 level3"
  echo "In the decreasing order: level1 > level2 > level3"
  echo "Type -h or --help for the full help."
  exit 0
}

notify () {
    dunstify -t 4000 -i "$battery_20_icon" -a "System" "Careful" "Battery level: $1%"
}

battery_20_icon="/usr/share/icons/Papirus-Dark/symbolic/status/battery-level-20-symbolic.svg"
# battery_critical_icon="/usr/share/icons/Papirus-Dark/symbolic/status/battery-level-10-symbolic.svg"
level=("$@")
state_path="/tmp/state.battery"
capacity="$(cat "/sys/class/power_supply/BAT0/capacity")"
reached_level="$(cat "$state_path")"
status="$(cat "/sys/class/power_supply/BAT0/status")"

if [ ${#level[@]} -eq 0 ] # If the array is empty: no arguments have been passed
then
   echo "Error using the script"
   echo "Please enter arguments"
   exit 1
fi


# If the file doesn't exist, I create it
if [ ! -f "$state_path" ]; then
    echo "0" > "$state_path"
fi

if [ "$status" = "Charging" ]; then
    echo "0" > "$state_path"
else
    # for loop on array's items and write the state in a file in /tmp
    for (( i=0; i < "${#level[@]}"; i++ ));
    do
        if [ "$capacity" -le "${level["$i"]}" ] && [ "$reached_level" -lt "$(($i + 1))" ]
        then
            notify "$capacity"
            echo "$(($i + 1))" > "$state_path"
        fi
    done
fi
