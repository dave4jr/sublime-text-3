#*============================
#*  Author:			Dave Luke Jr
#*  Company:		CenterStack.io
#*  Description:		Django Settings
#*============================
import os, sys
import socket


# ==================================================#
#	Path
# ==================================================#
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app_path = os.path.join(path, 'apps')

if path not in sys.path:
	sys.path.append(path)

if app_path not in sys.path:
	sys.path.append(app_path)


# ==================================================#
#	Deployment
# ==================================================#
if socket.gethostname() == 'davejr-mac.local':
	DEBUG = True
	INTERNAL_IPS = ('127.0.0.1')
	ALLOWED_HOSTS = []
else:
	DEBUG = False
	ALLOWED_HOSTS = ["www.centerstack.io"]
	ADMINS = MANAGERS = [("Dave Luke", "dave@centerstack.io")]


# ==================================================#
#	Roots
# ==================================================#
BASE_DIR 							= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT	 					= os.path.join(BASE_DIR, 'static', 'media')
STATIC_ROOT	 					= os.path.join(BASE_DIR, 'static', 'static_root')
STATIC_URL 						= '/static/'
MEDIA_URL	 						= '/media/'
LOGIN_URL							= 'login'
LOGOUT_URL						= 'index'
LOGIN_REDIRECT_URL 				= 'index'
SITE_ID							= 1


# ==================================================#
#	Directories
# ==================================================#
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static', 'static_dirs'),
	os.path.join(BASE_DIR, 'apps','aura','static', 'static_dirs'),
)
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
			os.path.join(BASE_DIR, 'apps','aura','templates'),
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				"django.template.context_processors.media",
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.csrf',
			],
		},
	},
]

# ==================================================#
#	Installed Apps / Middleware / Databases
# ==================================================#
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'tags',
	'aura',
	'blog',
	'newsletter',
	'planner',
	'contact',
	'widget_tweaks',
	'tinymce',
)


# ==================================================#
#	Middleware Classes
# ==================================================#
MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

# ==================================================#
#	Databases
# ==================================================#
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}



# ==================================================#
#	Application Settings
# ==================================================#
TINYMCE_JS_URL = STATIC_URL + 'plugins/tinymce/tinymce.min.js'
TINYMCE_JS_ROOT = STATIC_URL + 'plugins/tinymce'
TINYMCE_SPELLCHECKER = True
TINYMCE_DEFAULT_CONFIG = {
	'plugins': "spellchecker, code, colorpicker, importcss, insertdatetime, print, lists, link, preview, save, searchreplace, table, textcolor, wordcount",
	'theme': "modern",
	'cleanup_on_startup': True,
	'custom_undo_redo_levels': 20,
}
SESSION_SECURITY_WARN_AFTER			= 960
SESSION_SECURITY_EXPIRE_AFTER		= 1600
SESSION_EXPIRE_AT_BROWSER_CLOSE		= True

# ==================================================#
#	Date and Time Settings
# ==================================================#
TIME_ZONE 						= 'America/Los_Angeles'
TIME_FORMAT						= 'g:i A'
DATE_FORMAT		 				= 'N j, Y'
DATETIME_FORMAT					= 'N j, Y - g:i A'

TIME_INPUT_FORMATS 				= ('%I:%M %p',)
DATE_INPUT_FORMATS 				= ('%m/%d/%Y', '%b %d, %Y')
DATETIME_INPUT_FORMATS				= ('%m/%d/%Y, %I:%M %p')

USE_I18N 							= False
USE_L10N 							= False
USE_TZ 							= True


# ==================================================#
#	Django Debug Toolbar
# ==================================================#
if DEBUG:
	INSTALLED_APPS += ( 'debug_toolbar',)
	DEBUG_TOOLBAR_PANELS = [
		'debug_toolbar.panels.logging.LoggingPanel',
		'debug_toolbar.panels.request.RequestPanel',
		'debug_toolbar.panels.templates.TemplatesPanel',
		'debug_toolbar.panels.sql.SQLPanel',
		'debug_toolbar.panels.redirects.RedirectsPanel',
	]
	DEBUG_TOOLBAR_CONFIG = {
		"JQUERY_URL": "//ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js",
		"SHOW_COLLAPSED": True,
	}
	LOGGING = {
		 'version': 1,
		 'disable_existing_loggers': False,
		 'incremental': True,
		 'root': {
			  'level': 'DEBUG',
		 },
	}


# ==================================================#
#	Preferences
# ==================================================#
ROOT_URLCONF 					= 'main.urls'
WSGI_APPLICATION 					= 'main.wsgi.application'
LANGUAGE_CODE 					= 'en-us'
SECRET_KEY 						= 't1n$sjb$ql8pxcx$k!ewrbjy33+=kjsa*cn3pzqfy_iw*xt^t@'

