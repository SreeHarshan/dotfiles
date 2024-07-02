#!/bin/bash

zscroll --before-text " x" --delay 0.2 -l 15 \
		--match-command "Projects2/spotifox/cli_app.py --status" \
		--match-text "Playing" "--before-text ' '" \
		--match-text "Paused" "--before-text ' ' --scroll 0" \
		--update-check true "Projects2/spotifox/cli_app.py --get" &

wait

