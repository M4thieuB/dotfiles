# Created by newuser for 5.9

# STARTING COMMAND
eval "$(starship init zsh)"
pokemon-colorscripts -r

## PLUGIN
source $HOME/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source $HOME/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $HOME/.config/zsh/spaceship-prompt/spaceship.zsh


## ALIASES ##
alias ll="exa --icons -gal --group-directories-first"
alias ls="exa --icons -g --group-directories-first"
alias tree="exa --icons -g --tree --group-directories-first"
alias ..="cd .."

# Dotfiles repo alias
alias config="/usr/bin/git --git-dir=dotfiles.git --work-tree=$HOME"

alias cp="cp -i"
alias rm="rm -i"

# Emacs aliases
# alias emacs="emacsclient -c -a 'emacs'"

# changes the editor in the terminal, to edit long commands.
export EDITOR='emacsclient -nw -c -a "emacs"'
export VISAL='emacsclient -nw -c -a "emacs"'

# PATH CONFIG
export PATH="$HOME/.local/bin:$HOME/.emacs.d/bin:$PATH"

### "bat" as manpager
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
