#!/usr/bin/zsh

s=$(< /sys/class/power_supply/BAT0/status)
if [ $s = "Discharging" ]
then
    i3-msg "workspace 1"
    pavucontrol&|
elif
then
    zsh ~/.config/starter.sh
fi
