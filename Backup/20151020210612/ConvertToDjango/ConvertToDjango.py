#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Convert to Static
#*========================== #
import os, sys, codecs, re, shutil, zipfile, urllib2, urllib
from pprint import pprint as pp
import bs4, pyautogui
from django.conf import settings
import sublime, sublime_plugin
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


# ==================================================#
#	Sublime Plugin Class
# ==================================================#
class ConvertToDjangoCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.options = [
			"Convert To Django Syntax",
			"Generate 'urls.py' & 'views.py'",
			"Restore Template Files"
		]
		self.show_quick_panel(self.options)


	def on_menu_click(self, action):
		print("Sup G")

		# if action < 0:
		# 	return

		# elif action == 0:
		# 	items = [
		# 		["Open Project in New Window", "Open project in a new window"],
		# 		["Append Project", "Append project to current window"],
		# 		["Edit Project", "Edit project settings"],
		# 		['Rename Project', "Rename project"],
		# 		["Remove Project", "Remove from Project Manager"]
		# 	]



class CreateURLSCommand(sublime_plugin.WindowCommand):

	def run(self):
		print("Sup G")




class CreateViewsCommand(sublime_plugin.WindowCommand):

	def run(self):
		print("Sup G")




class RestoreTemplateFilesCommand(sublime_plugin.WindowCommand):

	def run(self):
		print("Sup G")




