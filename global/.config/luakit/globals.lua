-- Global settings for luakit
local globals = {
	homepage            = "http://home.jordynsblog.org/",
	new_tab_page        = "http://home.jordynsblog.org/",
	scroll_step         = 60,
	zoom_step           = 0.1,
	max_cmd_history     = 100,
	max_srch_history    = 100,
	vertical_tab_width  = 200,
	term                = "urxvt",
}

-- List of search engines to use, %s is replaced by the URL formatted search query.
globals.search_engines = {
    duckduckgo  = "https://duckduckgo.com/?q=%s",
    google      = "https://google.com/search?q=%s",
}

-- Set google as default search engine
globals.search_engines.default = globals.search_engines.google

-- Per-domain website properties.
globals.domain_props = {
	["all"] = {
		enable_scripts = false,
		enable_plugins = false,
	},

	["youtube.com"] = {
		enable_javascript = true,
	},

	["facebook.com"] = {
		enable_javascript = true,
	},

	["m.facebook.com"] = {
		enable_javascript = true,
	},

	["reddit.com"] = {
		enable_javascript = true,
	},

	["tparser.org"] = {
		enable_javascript = true,
	},

	["store.steampowered.com"] = {
		enable_javascript = true,
	},

	["steamcommunity.com"] = {
		enable_javascript = true,
	},

	["groups.google.com"] = {
		enable_javascript = true,
	},
}

-- Don't accept thrid party cookies.
soup.accept_policy = "no_third_party"

-- Cookie storage location.
soup.cookies_storage = luakit.data_dir .. "/cookies.db"

-- Used for internal luakit functions.
return globals
