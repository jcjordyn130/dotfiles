def set_keybindings(config):
        # Delete all keybindings.
        config.set("bindings.default", {})

        # Keybindings for normal mode.
        # Open a URL with o
        config.bind("o", "set-cmd-text -s :open")
        
        # Enter command mode with c.
        config.bind("c", "set-cmd-text :")
        
        # Enter insert mode with i.
        config.bind("i", "enter-mode insert")

        # Leave the current mode on Escape.
        for mode in ["command", "insert", "yesno"]:
                config.bind("<Escape>", "leave-mode", mode = mode)

        # Search on s.
        config.bind("s", "set-cmd-text :search ")

        # Go to the next result on n.
        config.bind("n", "search-next")

        # Go the the previous result on p.
        config.bind("p", "search-prev")

        # Go back and forward with b and f.
        config.bind("ub", "back")
        config.bind("uf", "forward")

        # Reload the current page with r.
        config.bind("ur", "reload")

        # Edit the current URL.
        config.bind("ue", "edit-url")
        
        # Open a new tab.
        config.bind("tn", "set-cmd-text -s :open -t")
        
        # Close the current tab.
        config.bind("tc", "tab-close")
        
        # Close all but the current tab.
        config.bind("ta", "tab-only")
        
        # Clone the current tab.
        config.bind("tC", "tab-clone")
        
        # Clear downloads.
        config.bind("dc", "download-clear")
        
        # Cancel the current download.
        config.bind("dC", "download-cancel")
        
        # Open the current download.
        config.bind("do", "download-open")
        
        # Retry the current download.
        config.bind("dr", "download-retry")
        
        # Delete the current download.
        config.bind("dd", "download-delete")
        
        # Yank the current URL into the clipboard
        config.bind("y", "yank")
        
        # Zoom in and out.
        config.bind("zo", "zoom-out")
        config.bind("zi", "zoom-in")
        config.bind("zd", "zoom")

        # Hint all links and open them in the background.       
        config.bind(";b", "hint links tab-bg")

        # Hint all links and open them with mpv.
        config.bind(";m", "hint links spawn /bin/bash -c 'mpv <(youtube-dl -o - {hint-url} 2>/dev/null | ~/code/yt_cache/cache.py)'")

        # Go up and down the tab list.
        config.bind("<Shift+Up>", "tab-prev")
        config.bind("<Shift+Down>", "tab-next")
        
        # Move a tab up and down the tab list.
        config.bind("<Ctrl+Up>", "tab-move -")
        config.bind("<Ctrl+Down>", "tab-move +")
        
        # Keybindings for command mode.
        # Run the command on Return.
        config.bind("<Return>", "command-accept", mode = "command")
        
        # Navigate the command history/completions with Up/Down.
        config.bind("<Up>", "completion-item-focus prev", mode = "command")
        config.bind("<Down>", "completion-item-focus next", mode = "command")

        # Keybindings for yes/no mode.
        config.bind("y", "prompt-accept yes", mode = "yesno")
        config.bind("n", "prompt-accept no", mode = "yesno")

        # Keybindings for tor.
        config.bind("ve", "set content.proxy socks://localhost:9050")
        config.bind("vd", "set content.proxy system")
