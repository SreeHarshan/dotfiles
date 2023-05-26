#!/usr/bin/zsh
s=$(< /sys/class/power_supply/BAT1/status)
if [ $s = "Discharging" ]
then
    pavucontrol&|
    xrandr --output eDP --mode 2560x1440_60.00
elif
then
    zsh ~/.config/starter.sh
fi
