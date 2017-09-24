" Disable vi compatibilty.
	set nocompatible
" Setup Vundle.
	set rtp+=~/.vim/bundle/Vundle.vim
	call vundle#begin()
" let Vundle manage Vundle, required
	Plugin 'VundleVim/Vundle.vim'
" Setup plugin vim-indent-guides.
	Plugin 'nathanaelkane/vim-indent-guides'
	" Enable plugin at startup.
	let g:indent_guides_enable_on_vim_startup = 1
	" Turn off auto color selection.
	let g:indent_guides_auto_colors = 0
	" Use the color grey for odd indenting.
	autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  ctermbg=grey
	" Use the color darkgrey for even indenting.
	autocmd VimEnter,Colorscheme * :hi IndentGuidesEven ctermbg=darkgrey
" End Vundle Setup.
	call vundle#end()
" can put buffer to the background without writing
" to disk, will remember history/marks.
	set hidden
" Send more commands to the tty at a given time.
	set ttyfast
" Show line numbers.
	set number
" Turn on syntax highlighting.
	syntax on
" Turn on highlight matching [{()}].
	set showmatch
" Set the tabstop to 4.
	set tabstop=4
" Set the color scheme to ron.
	:color ron
" Highlight the current line.
	set cursorline
" Redraw only when we need to.
	set lazyredraw
" Set the terminal/dvtm title.
	if has('title')
		set titlestring=
		set titlestring+=%t\ \(Vim\)
		set title
	endif
" Remove the bells.
	set noerrorbells
	set novisualbell
" Don't wrap lines.
	set nowrap
" Allow the command input box to take up two lines.
	set cmdheight=2
" Wrap lines without line breaks.
	set wrap
	set linebreak
	set textwidth=0
	set wrapmargin=0
