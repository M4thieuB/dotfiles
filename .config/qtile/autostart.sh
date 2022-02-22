#!/bin/sh

# Launch picom
picom --experimental-backends &

numlockx on 

# Launch nitrogen
nitrogen --restore &
