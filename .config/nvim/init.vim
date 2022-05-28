:set number
:set autoindent
:set softtabstop=4
:set mouse=a

"Gestion des plugins
call plug#begin()

Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/terryma/vim-multiple-cursors' "C-n for multiple cursor
Plug 'https://github.com/preservim/tagbar' "Tagbar
Plug 'https://github.com/ryanoasis/vim-devicons' " Developer Icons
Plug 'https://github.com/rafi/awesome-vim-colorschemes' "Collection of themes
Plug 'https://github.com/vim-airline/vim-airline-themes' "Collection of themes for airline


call plug#end()

:set termguicolors
:set t_Co=256

"Theme
:colorscheme deep-space
let g:airline_theme='deus'

"Raccourci pour lancer Tagbar
nmap <F8> :TagbarToggle<CR>

"Raccourci pour lancer NERDTree
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
