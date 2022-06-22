if status is-interactive

   # Adding important commands to the PATH env variable
   fish_add_path -mP $HOME/.emacs.d/bin
   fish_add_path -mP $HOME/scripts


# Defining handy aliases
   alias ll 'exa --icons -gal --group-directories-first'
   alias tree 'exa --icons -g --tree --group-directories-first'
   alias ls='exa -g --icons --group-directories-first'

# Opening emacs through a terminal (I use the client in order to open the GUI faster)
   alias emacs 'emacsclient -c -a "emacs"'


   alias cp 'cp -i'
   alias rm 'rm -i'


end
