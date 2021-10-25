#!/usr/bin/zsh

s=$(< /sys/class/power_supply/BAT0/status)
if [ $s = "Discharging" ]
then
    pavucontrol&|
elif
then
#    discord&|
    pavucontrol&|
    easyeffects&|
    deluge&|
    alacritty --class ncmpcpp --command ncmpcpp &|
    alacritty --class cava --command cava &|
    alacritty --class btm --command btm &|
fi
