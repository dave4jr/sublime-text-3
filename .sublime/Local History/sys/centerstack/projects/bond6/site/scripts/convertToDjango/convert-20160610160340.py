#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Convert to Django
#*========================== #
import os, sys, codecs, re, shutil, zipfile, urllib2, urllib
import urlparse
from easydict import EasyDict
from pprint import pprint as pp
import bs4, pyautogui
sys.stdout = codecs.getwriter('utf8')(sys.stdout)


class InitVariables():
	def __init__(self):

		#	Constant Settings
		# ===============================================
		self.PARSER				= "lxml"
		self.AUTHOR				= "CenterStack"
		self.TITLE					= "Bond6 Fitness"
		self.COUNTER				= 0
		self.RESTORE_WARNING		= False
		self.STATIC					= "{% load staticfiles %}"
		self.LINK_ATTRIBUTES			= ["href", "src", "data-src", "data-src-retina"]

		#	Input Settings
		# ========================================= #
		self.PROJECT				= "bond6"
		self.APP_NAME				= "sudo"
		
		#	Calculated Settings
		# ========================================= #
		self.THEME_DIR				= "/sys/centerstack/templates/%s/templates" % self.APP_NAME
		self.APP_DIR				= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'apps', self.APP_NAME)
		self.STATIC_DIR				= os.path.join(self.APP_DIR, 'static', 'static_dirs', self.APP_NAME)
		self.THEME					= self.get_templates(self.THEME_DIR)
		self.THEME_FILES			= self.THEME.files
		self.TEMPLATE_DIR			= os.path.join(self.APP_DIR, "templates", self.APP_NAME)
		self.TEMPLATE_FILES			= self.get_templates(self.TEMPLATE_DIR).files
		self.TEMPLATE_BACKUP		= "/sys/centerstack/site/scripts/convertToDjango/backups/%s.zip" % self.APP_NAME if self.PROJECT == "centerstack" else "/sys/centerstack/projects/%s/site/scripts/convertToDjango/backups/%s.zip" % (self.PROJECT, self.APP_NAME)

	def is_template(self, file):
		return True if file.lower().endswith('.html') else False

	def get_templates(self, dir):
		'''
		templates 				= object that contains the file, filename, folder instances
		templates.files 			= file instance
		templates.filenames 		= filename instance
		templates.folder 			= folder instance
		'''
		templates = EasyDict()
		templates_files = []
		templates_filenames = []
		templates_folders = []
		templates_folderfiles = []
		templates_transferNames = []

		for root, dirs, filenames in os.walk(dir):
			for filename in filenames:
				if self.is_template(filename):
					path = os.path.join(root, filename)
					folderfile = path[(len(dir)+1):len(path)]
					transferNames = folderfile.replace("/", "_").replace("_", "-")

					templates_files.append(path)
					templates_filenames.append(filename)
					templates_folderfiles.append(folderfile)
					templates_transferNames.append(transferNames)

		templates.files = templates_files
		templates.filenames = templates_filenames
		templates.folderfiles = templates_folderfiles
		templates.transferNames = templates_transferNames
		
		return templates


	def get_template_components(self):

		tc = EasyDict()
		bn_templates = []
		abs_templates = []
		folders = []

		templates = self.get_templates(self.THEME_DIR)
		files = templates.files
		transferNames = templates.transferNames

		for ii in range(len(files)):

			# Getting the folder using the html files from the theme directory
			bn_themefile = os.path.basename(files[ii])
			abs_themefile = files[ii]
			folder = abs_themefile[len(self.THEME_DIR)+1:len(abs_themefile)-len(bn_themefile)-1].replace("/","-").replace("_","-")
			basename, ext = os.path.splitext(bn_themefile)
			# Once we have the folder, now we can transfer everything back to the template_dir folder
			bn_templates.append(transferNames[ii])
			abs_templates.append(os.path.join(self.TEMPLATE_DIR, transferNames[ii]))
			folders.append(folder)
			

		tc.basename = bn_templates
		tc.absolute = abs_templates
		tc.folder = folders

		return tc


# ==================================================#
#	Transfer Tempalte Files
# ==================================================#
class TransferTemplateFiles(InitVariables):
	def run(self):
		templates = self.get_templates(self.THEME_DIR)
		files = templates.files
		transferNames = templates.transferNames

		zip = zipfile.ZipFile(self.TEMPLATE_BACKUP, mode='w')

		for ii in range(len(files)):
			transferPath = os.path.join(self.TEMPLATE_DIR, transferNames[ii])
			shutil.copy(files[ii], transferPath)
			zip.write(transferPath, os.path.basename(transferPath))
		zip.close()

		print "[*]  Template files have been transfered to Django templates folder!\n"
		print "[*]  A backup zip file, '%s', containing all of the newly transferred template files has been created and saved to '%s'!\n" % (os.path.basename(self.TEMPLATE_BACKUP), self.TEMPLATE_BACKUP)


# ==================================================#
#	Reload new copies of all the templates in the templates folder
# ==================================================#
class RestoreTemplateFiles(InitVariables):
	def run(self):
		response = pyautogui.confirm("Restore Template Files?") if self.RESTORE_WARNING else "OK"
		if  response == "OK":
			k = 1
			print "[*] Removing Current Template Files...\n------------------------------------"
			for file in self.TEMPLATE_FILES:
				os.remove(file)
				print "%s) %s" % (k, file)
				k += 1
				
			with zipfile.ZipFile(self.TEMPLATE_BACKUP, "r") as z:
				print "\n[*] Extracting Backup Template Files..."
				z.extractall(self.TEMPLATE_DIR)

			try:
				shutil.rmtree(os.path.join(self.TEMPLATE_DIR,"__MACOSX"))
				print "\n[*] Removing __MACOSX file"
			except:
				pass
		print "\n[*] Process Complete (%s of %s Template Files Restored).\n" % (k - 1, len(self.TEMPLATE_FILES))


# ==================================================#
#	Compile Source to Django Static Tags
# ==================================================#
class ConvertToDjango(InitVariables):

	def create_soup(self, template):
		self.f = open(template,'r+')
		self.soup = bs4.BeautifulSoup(self.f, self.PARSER,from_encoding="utf-8")
			
	def insert_load_static_declaration(self):
		try:
			html_tag = self.soup.find("html")
			html_tag.insert_before(self.STATIC)
		except:
			pass

	def compile_meta(self):
		try:
			self.soup.find("meta",{"name":"author"})['content'] = self.AUTHOR
		except:
			pass

		try:
			if self.TITLE == "default":
				pass
			else:
				self.soup.find("title").string = self.TITLE
		except:
			print "[!]  Note: title tag does not exist in this HTML Template. Please manually add this in the <head> as it is an important element to any template file!"

	def compile_links(self, folder):
		for attribute in self.LINK_ATTRIBUTES:
			attrs = self.soup.find_all(attrs = {attribute: True})

			# Check to see if link path starts with double dots (..) and if so, remove
			for attr in attrs:
				tag = attr[attribute]
				if tag[0:6] == "../../":
					tag = tag[6:]
				elif tag[0:3] == "../":
					tag = tag[3:]
				elif tag[0:1] == "/":
					tag = tag[1:]

				try:
					f, ext = os.path.splitext(tag)
				except:
					pass

				# Check if link is a static reference or a template HTML file
				if os.path.isfile(os.path.join(self.STATIC_DIR, tag)):
					attr[attribute] = "{%% static '%s/%s' %%}" % (self.APP_NAME, tag)
				elif ext == ".html" and tag[0:4] != "http":
					if folder:
						url = "%s-%s-%s" % (self.APP_NAME, folder, f)
						url = url.replace("/","-").replace("_", "-")
						attr[attribute] = "{%% url '%s' %%}" % url
					else:
						url = "%s-%s" % (self.APP_NAME, f)
						url = url.replace("/","-").replace("_", "-")
						attr[attribute] = "{%% url '%s' %%}" % url
				else:
					pass

	def save(self, template):
		try:
			self.f.close()
			html = self.soup.prettify("utf-8")
			with open(template, "wb") as file:
				 file.write(html)
		except:
			pass

	def run(self):
		try:
			tc = self.get_template_components()
			template_files = tc.absolute
			folders = tc.folder

			for ii in range(len(template_files)):

				template_file = template_files[ii]
				folder = folders[ii]

				# Checks to see if template has been compiled already
				self.create_soup(template_file)
				if re.search(self.STATIC, self.soup.prettify()):
					print "%s --- Already Processed! Skipping..." % os.path.basename(template_file)
				else:
					self.insert_load_static_declaration()
					self.compile_meta()
					self.compile_links(folder)
					self.save(template_file)
					print os.path.basename(template_file)
				self.COUNTER += 1
			print "\nProcess Complete!\n"
		except Exception, e:
			print e


# ==================================================#
#	Generate URL Conf
# ==================================================#
class CreateURLCONF(InitVariables):
	def run(self):
		urlconfs = []
		for theme in self.THEME_FILES:
			folder_file = theme[(len(self.THEME_DIR)+1):len(theme)]

			# Creating the 3 sections of the URLConf
			conf_url, ext = os.path.splitext(folder_file)
			conf_template = folder_file.replace("/","_").replace("_", "-")
			conf_name = "%s-%s" % (self.APP_NAME, conf_url.replace("/","_").replace("_", "-"))

			urlconf = "url(r'^%s/$', %s_views.main, {\"template\":\"%s\"}, name=\"%s\")," % (conf_url, self.APP_NAME, conf_template, conf_name)
			urlconfs.append(urlconf)

		k = 1
		print "from django.conf.urls import url, include"
		print "from . import views as %s_views" % self.APP_NAME
		for ii in range(len(urlconfs)):
			if k == 1:
				print "urlpatterns = ("
				print "	%s" % urlconfs[ii]
				k += 1
			if k < 250:
				print "	%s" % urlconfs[ii]
				k += 1
			if k == 250:
				print "	%s\n)\n\n" % urlconfs[ii]
				k = 1


# ==================================================#
#	Test
# ==================================================#
	def test(self):
		templates = self.get_templates(self.TEMPLATE_DIR).files
		print templates

		# for ii in range(len(files)):
		# 	transferPath = os.path.join(self.TEMPLATE_DIR, transferNames[ii])
		



# ==================================================#
#	Run
# ==================================================#
def run(action):
	actions = ["convert","con","urlconf","url","transfer","tr","restore","re","init", "test"]
	if action not in actions and not action.isspace():
		print "Action must be choosen from one of the following keywords: convert, urlconf, transfer, or restore"
	elif action in ["convert", "con"]:
		ConvertToDjango().run()
	elif action in ["urlconf", "url"]:
		CreateURLCONF().run()
	elif action in ["transfer", "tr"]:
		TransferTemplateFiles().run()
	elif action in ["restore", "re"]:
		RestoreTemplateFiles().run()
	elif action == "init":
		InitVariables()
	elif action == "test":
		InitVariables()
	else:
		print "Please enter an action into the run function!"
	
run("convert")




