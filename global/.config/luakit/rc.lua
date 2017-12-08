require "lfs"

if unique then
    unique.new("org.luakit")
    -- Check for a running luakit instance
    if unique.is_running() then
        if uris[1] then
            for _, uri in ipairs(uris) do
                if lfs.attributes(uri) then uri = os.abspath(uri) end
                unique.send_message("tabopen " .. uri)
            end
        else
            unique.send_message("winopen")
        end
        luakit.quit()
    end
end

-- Set the number of web processes to use. A value of 0 means 'no limit'.
luakit.process_limit = 8

-- Load library of useful functions for luakit
local lousy = require "lousy"

-- Load users global config
-- ("$XDG_CONFIG_HOME/luakit/globals.lua" or "/etc/xdg/luakit/globals.lua")
local globals = require "globals"

-- Load users theme
-- ("$XDG_CONFIG_HOME/luakit/theme.lua" or "/etc/xdg/luakit/theme.lua")
lousy.theme.init(lousy.util.find_config("theme.lua"))
assert(lousy.theme.get(), "failed to load theme")

-- Load users window class
-- ("$XDG_CONFIG_HOME/luakit/window.lua" or "/etc/xdg/luakit/window.lua")
local window = require "window"

-- Load users webview class
-- ("$XDG_CONFIG_HOME/luakit/webview.lua" or "/etc/xdg/luakit/webview.lua")
local webview = require "webview"

-- Add luakit://log/ chrome page
local log_chrome = require "log_chrome"

window.add_signal("build", function (w)
    local widgets, l, r = require "lousy.widget", w.sbar.l, w.sbar.r

    -- Left-aligned status bar widgets
    l.layout:pack(widgets.uri())
    l.layout:pack(widgets.hist())
    l.layout:pack(widgets.progress())

    -- Right-aligned status bar widgets
    r.layout:pack(widgets.buf())
    r.layout:pack(log_chrome.widget())
    r.layout:pack(widgets.ssl())
    r.layout:pack(widgets.tabi())
    r.layout:pack(widgets.scroll())
end)

-- Load luakit binds and modes
local modes = require "modes"
local binds = require "binds"

-- Load local keybindings.
local local_binds = require "local_binds"

-- Move the tab bar to the side.
local vertical_tabs = require "vertical_tabs"

-- Add adblock support
local adblock = require "adblock"
local adblock_chrome = require "adblock_chrome"

-- F12 debug tools support.
local webinspector = require "webinspector"

-- Add uzbl-like form filling
local formfiller = require "formfiller"

-- Add quickmarks support & manager
local quickmarks = require "quickmarks"

-- Add session saving/loading support
local session = require "session"

-- Add command to list closed tabs & bind to open closed tabs
local undoclose = require "undoclose"

-- Add command to list tab history items
local tabhistory = require "tabhistory"

-- Add greasemonkey-like javascript userscript support
local userscripts = require "userscripts"

-- Add bookmarks support
local bookmarks = require "bookmarks"
local bookmarks_chrome = require "bookmarks_chrome"

-- Add download support
local downloads = require "downloads"
local downloads_chrome = require "downloads_chrome"

-- Add automatic PDF downloading and opening
local viewpdf = require "viewpdf"

-- Example using xdg-open for opening downloads / showing download folders
downloads.add_signal("open-file", function (file)
    luakit.spawn(string.format("xdg-open %q", file))
    return true
end)

-- Add vimperator-like link hinting & following
local follow = require "follow"

-- Add command history
local cmdhist = require "cmdhist"

-- Add search mode & binds
local search = require "search"

-- Add ordering of new tabs
local taborder = require "taborder"

-- Add web history support
local history = require "history"
local history_chrome = require "history_chrome"

-- Add luakit://help support
local help_chrome = require "help_chrome"

-- Add command completion
local completion = require "completion"

local follow_selected = require "follow_selected"
local go_input = require "go_input"
local go_next_prev = require "go_next_prev"
local go_up = require "go_up"

-- Filter Referer HTTP header if page domain does not match Referer domain
require_web_module("referer_control_wm")

-- Add a consistent error page style
local error_page = require "error_page"

-- Add userstyles loader
local styles = require "styles"

-- Hide the scrollbars
local hide_scrollbars = require "hide_scrollbars"

-- Automatically apply per-domain webview properties
local domain_props = require "domain_props"

-- Add a stylesheet when showing images
local image_css = require "image_css"

-- Add a new tab page
local newtab_chrome = require "newtab_chrome"

-- Add tab favicons mod
local tab_favicons = require "tab_favicons"

-- Add :view-source command
local view_source = require "view_source"

-- Restore last saved session if we're the only luakit instance running.
local w = (not luakit.nounique) and (session and session.restore())
if w then
	-- Open the tabs back.
	for i, uri in ipairs(uris) do
		w:new_tab(uri, { switch = i == 1 })
	end
else
	-- Open a new session.
	window.new(uris)
end


-- Open URIs from other luakit instances
if unique then
    unique.add_signal("message", function (msg, screen)
        local cmd, arg = string.match(msg, "^(%S+)%s*(.*)")
        local ww = lousy.util.table.values(window.bywidget)[1]
        if cmd == "tabopen" then
            ww:new_tab(arg)
        elseif cmd == "winopen" then
            ww = window.new((arg ~= "") and { arg } or {})
        end
        ww.win.screen = screen
        ww.win.urgency_hint = true
    end)
end

-- Redirect all requests for the new tab page to our homepage.
webview.add_signal("init", function (view)
	view:add_signal("navigation-request", function (_, uri)
		if uri == "luakit://newtab/" then
			view.uri = globals.homepage
			return false
		end
	end)
end)

-- Block all new windows from any site that contains "thepiratebay" or "torrentproject".
webview.add_signal("init", function (view)
	view:add_signal("new-window-decision", function (_, uri)
		if string.find(view.uri, "thepiratebay") or string.find(view.uri, "torrentproject") then
			return false
		end
	end)
end)

-- Open magnet: URIs in deluge.
webview.add_signal("init", function (view)
	view:add_signal("navigation-request", function (v, uri)
		if string.match(string.lower(uri), "^magnet:") then
			luakit.spawn(string.format("%s %q", "deluge-gtk", uri))
			return false
		end
	end)
end)

-- Open youtube watch links in mpv
webview.add_signal("init", function (view)
	view:add_signal("navigation-request", function (v, uri)
		if string.find(uri, "https://www.youtube.com/watch") then
			luakit.spawn(string.format("mpv %q", uri))
			return false
		end
	end)
end)
