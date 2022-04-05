#!/usr/bin/zsh

pavucontrol&|
easyeffects&|
deluge&|
discord&|
alacritty --class ncmpcpp --command ncmpcpp &|;
sleep 0.3 && i3-msg "workspace 3" && i3-msg "layout splitv" && i3-msg "workspace back_and_forth" && alacritty --class cava --command cava&| 
alacritty --class btm --command btm &|
i3-msg "workspace 1"
#cd Projects/Fredric
#uvicorn server:app --reload --host 0.0.0.0 --port 8080
