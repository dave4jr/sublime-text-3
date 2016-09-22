   #!/usr/bin/python
# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import LiveReload


# def plugin_loaded():
# 	sublime.set_timeout(lambda : sublime.run_command("simple_reload_delay"), 10000)


class SimpleReloadDelayCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		index = 5
		LiveReload.Plugin.togglePlugin(index)
	
