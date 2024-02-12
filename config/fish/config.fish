cat ~/.cache/wal/sequences 

alias mpvgpu="prime-run mpv --profile=svp"
alias rr='ranger --choosedir=$HOME/.rangerdir; set LASTDIR (cat $HOME/.rangerdir); cd "$LASTDIR"'

if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Created by `pipx` on 2023-08-20 16:17:58
set PATH $PATH /home/harshan/.local/bin
