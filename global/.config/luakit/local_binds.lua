-- Core variables.
local window = require("window")
local globals = require("globals")

-- Binding aliases
local lousy = require("lousy")
local modes = require("modes")

-------------------------------------
-- Local key bindings.
------------------------------------
modes.add_binds("normal", {
	-- Closes the current tab on 'c'.
	{ "c", "Close current tab.", function (w) w:close_tab() end },

	-- History switching with 'b' and 'f'.
	{ "b", "Go back in the history.", function (w) w:back(1) end },
	{ "f", "Go forward in the history.", function (w) w:forward(1) end },

	-- Switches tabs on Shift + [up/down]
	{ "<Shift-Up>", "Switch to the previous tab.", function (w) w:prev_tab() end },
	{ "<Shift-Down>", "Switch to the next tab.", function (w) w:next_tab() end },

	-- Goes to the downloads page on 'd'.
	{ "d", "Opens the downloads page.", function (w) w:new_tab("luakit://downloads") end },

	-- Preinserts the command to google something on 'g'.
	{ "g", "Googles one or more queries.", function (w) w:enter_cmd(":open google ") end },

	-- Same thing as above but uses a new tab.
	{ "G", "Googles one or more queries in a new tab.", function (w) w:enter_cmd(":tabopen google ") end },

	-- Plays the current (or hovered) url in mpv on 'p'.
	{ "p", "Plays the current URL in mpv.", function (w) 
			local view = w.view
			local uri = view.hovered_uri or view.uri
			if uri then
				luakit.spawn(string.format("mpv %s", uri))
			end
	end },

	-- Copys selected text into the clipboard on 'Control + c'.
	{ "<Control-c>", "Copy selected text.", function () luakit.selection.clipboard = luakit.selection.primary end },
})
