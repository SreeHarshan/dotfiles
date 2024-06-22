cat ~/.cache/wal/sequences 

alias mpvgpu="prime-run mpv --profile=svp"
alias rr='ranger --choosedir=$HOME/.rangerdir; set LASTDIR (cat $HOME/.rangerdir); cd "$LASTDIR"'

#python ~/scripts/ascii_print.py

if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Created by `pipx` on 2023-08-20 16:17:58
set PATH $PATH /home/harshan/.local/bin

# flutter path
export PATH="$PATH:/home/harshan/flutter/bin"
export PATH="$PATH:/home/harshan/anaconda3/bin"


#export PATH="$PATH:/usr/bin"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/harshan/anaconda3/bin/conda
    eval /home/harshan/anaconda3/bin/conda "shell.fish" "hook" $argv | source
else
    if test -f "/home/harshan/anaconda3/etc/fish/conf.d/conda.fish"
        . "/home/harshan/anaconda3/etc/fish/conf.d/conda.fish"
    else
        set -x PATH "/home/harshan/anaconda3/bin" $PATH
    end
end
# <<< conda initialize <<<

