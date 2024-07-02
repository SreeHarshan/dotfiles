#!/bin/bash

wall_dir=~/Pictures/Wallpaper/slide_show
wall_path=$(find -L $wall_dir -type f | shuf -n 1)

~/.config/scripts/wallpaper/change_wallpaper.sh "$wall_path"
