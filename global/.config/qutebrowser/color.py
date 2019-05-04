# The Solarized Dark color theme.
class SolarizedDark():
        # These are the colors that make up the solarized theme.
        colors = {
            "base03": "#002b36",
            "base02": "#073642",
            "base01": "#586e75",
            "base00": "#657b83",
            "base0": "#839496",
            "base1": "#93a1a1",
            "base2": "#eee8d5",
            "base3": "#fdf6e3",
            "yellow": "#b58900",
            "orange": "#cb4b16",
            "red": "#dc322f",
            "magenta": "#d33682",
            "violet": "#6c71c4",
            "blue": "#268bd2",
            "cyan": "#2aa198",
            "green": "#859900"
        }

        def __init__(self, config):
            self.config = config

        def Apply(self):
            ## Background color of the completion widget category headers.
            self.config.colors.completion.category.bg = self.colors["base03"]

            ## Bottom border color of the completion widget category headers.
            self.config.colors.completion.category.border.bottom = self.colors["base03"]

            ## Top border color of the completion widget category headers.
            self.config.colors.completion.category.border.top = self.colors["base03"]

            ## Foreground color of completion widget category headers.
            self.config.colors.completion.category.fg = self.colors["base3"]

            ## Background color of the completion widget for even rows.
            self.config.colors.completion.even.bg = self.colors["base02"]

            ## Text color of the completion widget.
            self.config.colors.completion.fg = self.colors["base1"]

            ## Background color of the selected completion item.
            self.config.colors.completion.item.selected.bg = self.colors["violet"]

            ## Bottom border color of the selected completion item.
            self.config.colors.completion.item.selected.border.bottom = self.colors["violet"]

            ## Top border color of the completion widget category headers.
            self.config.colors.completion.item.selected.border.top = self.colors["violet"]

            ## Foreground color of the selected completion item.
            self.config.colors.completion.item.selected.fg = self.colors["base3"]

            ## Foreground color of the matched text in the completion.
            self.config.colors.completion.match.fg = self.colors["base2"]

            ## Background color of the completion widget for odd rows.
            self.config.colors.completion.odd.bg = self.colors["base02"]

            ## Color of the scrollbar in completion view
            self.config.colors.completion.scrollbar.bg = self.colors["base1"]

            ## Color of the scrollbar handle in completion view.
            self.config.colors.completion.scrollbar.fg = self.colors["base2"]

            ## Background color for the download bar.
            self.config.colors.downloads.bar.bg = self.colors["base03"]

            ## Background color for downloads with errors.
            self.config.colors.downloads.error.bg = self.colors["red"]

            ## Foreground color for downloads with errors.
            self.config.colors.downloads.error.fg = self.colors["base3"]

            ## Color gradient start for download backgrounds.
            self.config.colors.downloads.start.bg = "#0000aa"

            ## Color gradient start for download text.
            self.config.colors.downloads.start.fg = self.colors["base3"]

            ## Color gradient stop for download backgrounds.
            self.config.colors.downloads.stop.bg = "#00aa00"

            ## Background color for hints. Note that you can use a `rgba(...)` value
            ## for transparency.
            self.config.colors.hints.bg = self.colors["violet"]

            ## Font color for hints.
            self.config.colors.hints.fg = self.colors["base3"]

            ## Font color for the matched part of hints.
            self.config.colors.hints.match.fg = self.colors["base1"]

            ## Background color of the keyhint widget.
            # self.config.colors.keyhint.bg = "rgba(0, 0, 0, 80%)"

            ## Text color for the keyhint widget.
            self.config.colors.keyhint.fg = self.colors["base3"]

            ## Highlight color for keys to complete the current keychain.
            self.config.colors.keyhint.suffix.fg = self.colors["yellow"]

            ## Background color of an error message.
            self.config.colors.messages.error.bg = self.colors["red"]

            ## Border color of an error message.
            self.config.colors.messages.error.border = self.colors["red"]

            ## Foreground color of an error message.
            self.config.colors.messages.error.fg = self.colors["base3"]

            ## Background color of an info message.
            self.config.colors.messages.info.bg = self.colors["base03"]

            ## Border color of an info message.
            self.config.colors.messages.info.border = self.colors["base03"]

            ## Foreground color an info message.
            self.config.colors.messages.info.fg = self.colors["base3"]

            ## Background color of a warning message.
            self.config.colors.messages.warning.bg = self.colors["orange"]

            ## Border color of a warning message.
            self.config.colors.messages.warning.border = self.colors["orange"]

            ## Foreground color a warning message.
            self.config.colors.messages.warning.fg = self.colors["base3"]

            ## Background color for prompts.
            self.config.colors.prompts.bg = self.colors["base02"]

            ## Border used around UI elements in prompts.
            self.config.colors.prompts.border = "1px solid " + self.colors['base3']

            ## Foreground color for prompts.
            self.config.colors.prompts.fg = self.colors["base3"]

            ## Background color for the selected item in filename prompts.
            self.config.colors.prompts.selected.bg = self.colors["base01"]

            ## Background color of the statusbar in caret mode.
            self.config.colors.statusbar.caret.bg = self.colors["blue"]

            ## Foreground color of the statusbar in caret mode.
            self.config.colors.statusbar.caret.fg = self.colors["base1"]

            ## Background color of the statusbar in caret mode with a selection.
            self.config.colors.statusbar.caret.selection.bg = self.colors["violet"]

            ## Foreground color of the statusbar in caret mode with a selection.
            self.config.colors.statusbar.caret.selection.fg = self.colors["base1"]

            ## Background color of the statusbar in command mode.
            self.config.colors.statusbar.command.bg = self.colors["base03"]

            ## Foreground color of the statusbar in command mode.
            self.config.colors.statusbar.command.fg = self.colors["base1"]

            ## Background color of the statusbar in private browsing + command mode.
            self.config.colors.statusbar.command.private.bg = self.colors["base01"]

            ## Foreground color of the statusbar in private browsing + command mode.
            self.config.colors.statusbar.command.private.fg = self.colors["base3"]

            ## Background color of the statusbar in insert mode.
            self.config.colors.statusbar.insert.bg = self.colors["base02"]

            ## Foreground color of the statusbar in insert mode.
            self.config.colors.statusbar.insert.fg = self.colors["base1"]

            ## Background color of the statusbar.
            self.config.colors.statusbar.normal.bg = self.colors["base03"]

            ## Foreground color of the statusbar.
            self.config.colors.statusbar.normal.fg = self.colors["base1"]

            ## Background color of the statusbar in passthrough mode.
            self.config.colors.statusbar.passthrough.bg = self.colors["base02"]

            ## Foreground color of the statusbar in passthrough mode.
            self.config.colors.statusbar.passthrough.fg = self.colors["base1"]

            ## Background color of the statusbar in private browsing mode.
            self.config.colors.statusbar.private.bg = self.colors["base01"]

            ## Foreground color of the statusbar in private browsing mode.
            self.config.colors.statusbar.private.fg = self.colors["base3"]

            ## Background color of the progress bar.
            self.config.colors.statusbar.progress.bg = self.colors["base1"]

            ## Foreground color of the URL in the statusbar on error.
            self.config.colors.statusbar.url.error.fg = self.colors["red"]

            ## Default foreground color of the URL in the statusbar.
            self.config.colors.statusbar.url.fg = self.colors["base1"]

            ## Foreground color of the URL in the statusbar for hovered links.
            self.config.colors.statusbar.url.hover.fg = self.colors["base2"]

            ## Foreground color of the URL in the statusbar on successful load
            ## (http).
            self.config.colors.statusbar.url.success.http.fg = self.colors["base1"]

            ## Foreground color of the URL in the statusbar on successful load
            ## (https).
            self.config.colors.statusbar.url.success.https.fg = self.colors["base1"]

            ## Foreground color of the URL in the statusbar when there"s a warning.
            self.config.colors.statusbar.url.warn.fg = self.colors["yellow"]

            ## Background color of the tab bar.
            self.config.colors.tabs.bar.bg = self.colors["base03"]

            ## Background color of unselected even tabs.
            self.config.colors.tabs.even.bg = self.colors["base02"]

            ## Foreground color of unselected even tabs.
            self.config.colors.tabs.even.fg = self.colors["base1"]

            ## Color for the tab indicator on errors.
            self.config.colors.tabs.indicator.error = self.colors["red"]

            ## Color gradient start for the tab indicator.
            self.config.colors.tabs.indicator.start = self.colors["violet"]

            ## Color gradient end for the tab indicator.
            self.config.colors.tabs.indicator.stop = self.colors["orange"]

            ## Background color of unselected odd tabs.
            self.config.colors.tabs.odd.bg = self.colors["base03"]

            ## Foreground color of unselected odd tabs.
            self.config.colors.tabs.odd.fg = self.colors["base1"]

            ## Background color of selected even tabs.
            self.config.colors.tabs.selected.even.bg = self.colors["violet"]

            ## Foreground color of selected even tabs.
            self.config.colors.tabs.selected.even.fg = self.colors["base2"]

            ## Background color of selected odd tabs.
            self.config.colors.tabs.selected.odd.bg = self.colors["violet"]

            ## Foreground color of selected odd tabs.
            self.config.colors.tabs.selected.odd.fg = self.colors["base2"]
