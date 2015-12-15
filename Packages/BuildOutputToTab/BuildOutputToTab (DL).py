#*========================= #
#*  Author:	Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	BuildOutputToTab
#*========================= #
import os, sys
import sublime
import sublime_plugin
from . import exec

# sys.path.append(os.path.join(sublime.packages_path(), 'Default'))
# exe = __import__('exec')
# sys.path.remove(os.path.join(sublime.packages_path(), 'Default'))

class BuildOutputToTabCommand(sublime_plugin.WindowCommand):
	def run():
		build_output_to_tab = sublime.load_settings("Preferences.sublime-settings").get("build_output_to_tab", False)

		if build_output_to_tab:
			if hasattr(self, 'output_view') == False or -1 in self.window.get_view_index(self.output_view):
				self.output_view = self.window.new_file()
				self.output_view.set_name("Build Results")
				self.output_view.set_scratch(True)
			self.window.focus_view(self.output_view)


			if hasattr(self, 'proc'):
				self.append_data(self, self.proc, "\n\n\n")

		# exe.ExecCommand.run(self, cmd, file_regex, line_regex, working_dir, encoding, env, quiet, kill , **kwargs)



