" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.vim/plugged')

Plug 'tpope/vim-sensible'
Plug 'airblade/vim-gitgutter'
Plug 'dylanaraps/wal.vim'
Plug 'ryanoasis/vim-devicons'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'jlanzarotta/bufexplorer'
Plug 'tpope/vim-surround'
Plug 'vimwiki/vimwiki'
Plug 'dag/vim-fish'
Plug 'neoclide/coc.nvim', {'branch': 'master', 'do': 'yarn install --frozen-lockfile'}

" Initialize plugin system
call plug#end()

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" True color
" se termguicolors

" Colorscheme
 colo wal

" Indentation
se expandtab
se shiftwidth=4
se softtabstop=4

" Line numbers
" The default is relative line numbers
se nu rnu
" Toggle between relative and absolute line members
augroup numbertoggle
  autocmd!
  autocmd BufEnter,InsertLeave * set rnu
  " Uncomment to disable hybrid numbers
  " autocmd BufEnter,InsertLeave * set nonu
  autocmd BufLeave,InsertEnter * set nornu
  " Uncomment to disable hybrid numbers
  " autocmd BufLeave,InsertEnter * set nu
augroup END

" Map ctrl + c to copy selection to system clipboard
vnoremap <C-c> "+y
" Map tab to go to next buffer
nmap <Tab> :bn<cr>
" Map shift + tab to go to previous buffer
nmap <S-Tab> :bp<cr>
" Map jk to go to normal mode from insert mode
imap jk <Esc>

" configure vim-airline
let g:airline#extensions#tabline#enabled = 1
" let g:airline_theme = 'onedark'
" powerline symbols
let g:airline_powerline_fonts = 1

" Mappings for CoCList
" Show all diagnostics.
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions.
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
" Show commands.
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document.
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols.
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item.
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item.
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list.
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>

