# Setup the history file.
HISTFILE=~/.zsh_history
HISTSIZE=50
SAVEHIST=1024

# Misc options.
# Append to the history file.
setopt appendhistory 

# Change to a directory if given like a command.
setopt autocd 

# Use extended globbing.
setopt extendedglob

# Don't beep on an error.
unsetopt beep

# Don't error out on a non-matching glob.
unsetopt nomatch

# Notify about changes in background jobs at the beginning of a prompt (like bash)
unsetopt notify

# Setup Vi-like keybindings.
bindkey -v

# Set the default completion options.
zstyle :compinstall filename '/home/jordyn-void/.zshrc'
autoload -Uz compinit
compinit

# Setup the prompt.
autoload -U promptinit; promptinit

# If we're root make it red, else use the default.
if [ "$(id -u)" == "0" ]; then
	prompt fade red
else
	prompt fade
fi

# Setup our personal bin.
if [ -e "$HOME/bin" ]; then
	export PATH="$HOME/bin:$PATH"
fi

# Setup the EDITOR.
export EDITOR="vim"

# Aliases
# Logs into into my server via either ssh or mosh.
alias server="ssh jordynsblog.org -p 20"
alias server_mosh="mosh --ssh=\"ssh -p 20\" jordynsblog.org"

# Warn if the language isn't UTF-8.
if echo $LANG | grep US-ASCII >/dev/null 2>&1; then
	echo -e "\e[0;31mWARNING: \$LANG is set to ASCII, not UTF-8. \e[0m"
fi

# Run pygreeter.
pygreeter
