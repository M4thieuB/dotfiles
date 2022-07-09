# Created by newuser for 5.9

# STARTING COMMAND
eval "$(starship init zsh)"
pokemon-colorscripts -r

## PLUGIN
source ~/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source ~/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.config/zsh/spaceship-prompt/spaceship.zsh


## ALIASES ##
alias ll="exa --icons -gal --group-directories-first"
alias ls="exa --icons -g --group-directories-first"
alias tree="exa --icons -g --tree --group-directories-first"
alias ..="cd .."

# Dotfiles repo alias
alias config="/usr/bin/git --git-dir=dotfiles.git --work-tree=$HOME"

alias cp="cp -v"
alias rm="rm -i"

# Emacs aliases
# alias emacs="emacsclient -c -a 'emacs'"

# changes the editor in the terminal, to edit long commands.
export EDITOR='nvim'
export VISAL='nvim'

export QT_QPA_PLATFORMTHEME=qt5ct

# PATH CONFIG
export PATH="$HOME/.config/scripts:$HOME/.local/bin:$HOME/.emacs.d/bin:$PATH"

### "bat" as manpager
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Lines configured by zsh-newuser-install
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
# End of lines configured by zsh-newuser-install
