# dotfiles
My personal Manjaro config

I use qtile as my Window Manager, fish for my shell and kitty for my terminal. 

To install qtile: sudo pacman -S qtile
To install kitty: sudo pacman -S kitty
To install fish: sudo pacman -S fish

Dependencies :
picom-tryone-git, compositor allowing me to have a blur effect, rounded corner and transparency.
dunst, notification server allowing me to receive notifications on my system such as 'LOW BATTERY'
dbus-next is necessary for the battery notification 
Fira Nerd Font (available on github when searching Nered Font)

When it comes to the Arch Button at the top-right of my bar, I am using the dmenu script dm-logout which displays a menu
where I can choose if I want to reboot, logout, lock the screen, or shutdown my machine. One dependency is slock (and of
course dmenu).

My fish plugin are handled by omf (oh-my-fish). 

My editor is neovim. In order to work, it needs Vim-plug so it manages my plugin.

The brightness of my screen is managed by brightnessctl. Do not forget to give him acess to your video folder so you must not be root each time
you use it. 
I use amixer to control my sound. 

Nitrogen is managing my wallpapers. 

Thunar is my filemanager. 
