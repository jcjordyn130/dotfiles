from pathlib import Path
import color
import keybindings

# Make qutebrowser solarized.
colortheme = color.SolarizedDark(c)
colortheme.Apply()

# Set the keybindings.
keybindings.set_keybindings(config)

# Put the tabs on the left.
config.set("tabs.position", "left")

# Use my custom home page.
config.set("url.start_pages", ["about:blank"])

# Use my custom start page.
config.set("url.default_page", "about:blank")

# Set the HTTP cache to be 2147483647 bytes.
config.set("content.cache.size", 2147483647)

# Forward all unbound keys to the webview.
config.set("input.forward_unbound_keys", "all")

# Disable WebGL
config.set("content.webgl", False)

# Set the tab bar size
config.set("tabs.width", "12%")

# Set the tab title format.
config.set("tabs.title.format", "{title}")

# List of URL parameters to strip from the URL on yank.
config.set("url.yank_ignored_parameters", ["ref", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "feature", "keywords", ])

# Make the command completion.
config.set("completion.height", "25%")

# Don't load all restored tabs at once, as this causes a lot of CPU usage and other undesired effects.
config.set("session.lazy_restore", True)

# Send the DNT header to sites.
config.set("content.headers.do_not_track", True)

# Enable adblock.
config.set("content.host_blocking.enabled", True)

# Set the adblock lists.
config.set("content.host_blocking.lists", ["https://www.malwaredomainlist.com/hostslist/hosts.txt", "http://someonewhocares.org/hosts/hosts", "http://winhelp2002.mvps.org/hosts.zip", "http://malwaredomains.lehigh.edu/files/justdomains.zip", "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext", "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"])

# Set the downloads directory to "$HOME/Downloads" with pathlib.
home = Path.home() / "Downloads"
config.set("downloads.location.directory", str(home))

# Don't prompt for the download directory.
config.set("downloads.location.prompt", False)

# Don't show the scroll bar.
config.set("scrolling.bar", "never")

# Disable tab indicators.
config.set("tabs.indicator.width", 0)

# Set vim as the editor.
config.set("editor.command", ["urxvt", "-e", "vim", "{file}"])

# Set the search engines.
config.set("url.searchengines", {
	"DEFAULT": "https://duckduckgo.com/?q={}",
	"google": "https://www.google.com/search?q={}"
})

# Per domain settings.
# Enable WebGL on Facebook as certain games require it.
config.set("content.webgl", True, "*://facebook.com/")

# Disable JavaScript on any and every tor site.
config.set("content.javascript.enabled", False, "*://*.onion/*")
