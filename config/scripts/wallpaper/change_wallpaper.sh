#!/bin/bash

feh --bg-scale "$1"
wallust run "$1"
truncate -s 0 ~/.config/scripts/wallpaper/current_wall
echo "$1" >> ~/.config/scripts/wallpaper/current_wall

# Restart programs to change color scheme

pkill dunst
dunst&

~/.config/polybar/launch.sh
