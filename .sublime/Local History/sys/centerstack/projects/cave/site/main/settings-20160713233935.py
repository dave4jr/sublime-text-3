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
	INTERNAL_IPS = ('127.0.0.1:8000')
	ALLOWED_HOSTS = []
else:
	DEBUG = False
	ALLOWED_HOSTS = ["rms.coloradomotorcycleadventures.com"]
	ADMINS = MANAGERS = [("Dave Luke", "dave@centerstack.io")]



# ==================================================#
#	Server Settings
# ==================================================#
EMAIL_HOST 						= 'smtp.gmail.com'
EMAIL_HOST_USER 					= 'info@coloradomotorcycleadventures.com'
EMAIL_HOST_PASSWORD 				= 'C0Inf02422'
EMAIL_USE_SSL						= True
EMAIL_PORT 						= 465
EMAIL_BACKEND 					= 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER



# ==================================================#
#	Paths
# ==================================================#
BASE_DIR 							= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT	 					= os.path.join(BASE_DIR, 'static', 'media')
STATIC_ROOT	 					= os.path.join(BASE_DIR, 'static', 'static_root')
STATIC_URL 						= '/static/'
MEDIA_URL	 						= '/media/'
LOGIN_URL							= 'login'
LOGOUT_URL						= 'index'
LOGIN_REDIRECT_URL					= 'index'
SITE_ID							= 1


# ==================================================#
#	Date and Time Settings
# ==================================================#
TIME_ZONE 						= 'America/Denver'
TIME_FORMAT						= 'g:i A'
DATE_FORMAT		 				= 'N j, Y'
DATETIME_FORMAT					= 'N j, Y | g:iA'

TIME_INPUT_FORMATS 				= ('%I:%M %p',)
DATE_INPUT_FORMATS 				= ('%m/%d/%Y', '%b %d, %Y', '%Y-%m-%d')
DATETIME_INPUT_FORMATS				= ('%m/%d/%Y, %I:%M %p', '%m/%d/%Y - %I:%M%p', '%m/%d/%Y, %I:%M%p', '%Y-%m-%d %I:%M%p', '%Y-%m-%d %H:%M:%S')

USE_I18N 							= False
USE_L10N 							= False
USE_TZ 							= False


# ==================================================#
#	Directories
# ==================================================#
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static', 'static_dirs'),
)
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.request',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.csrf',
				'preferences.context_processors.preference',
				'account.context_processors.account',
			],
			
		},
	},
]







# ==================================================#
#	Middleware / Database
# ==================================================#
MIDDLEWARE_CLASSES = (
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'session_security.middleware.SessionSecurityMiddleware',
	'account.middleware.LocaleMiddleware',
	'account.middleware.TimezoneMiddleware',
 )
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}



# ==================================================#
#	Installed Applications
# ==================================================#
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'tags',
	'inventory',
	'preferences',
	'classes',
	'members',
	'reservations',
	'pos',
	'widget_tweaks',
	'colorfield',
	'mathfilters',
	'tinymce',
	'session_security',
	'django_xworkflows',
	'django_xworkflows.xworkflow_log',
	'django_extensions',
	'account',
)

# ==================================================#
#	Stripe
# ==================================================#
STRIPE_SECRET_KEY = "sk_test_DcjbI3p4rPtqgjtpvweYjXsE"
STRIPE_PUBLIC_KEY = "pk_test_6eKlYSUJZWIJnmPzHxp3qAYJ"





# ==================================================#
#	Application Preference
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
THUMBNAIL_ALIASES = {
	 '': {
		  'avatar': {'size': (50, 50), 'crop': True},
	 },
}
AUTH_PROFILE_MODULE = "profiles.UserProfile"
JSIGNATURE_COLOR = "#D05454"
JSIGNATURE_LINE_WIDTH = "0"
JSIGNATURE_RESET_BUTTON = False


# ==================================================#
#	Django Debug Toolbar
# ==================================================#
if DEBUG:
	INSTALLED_APPS += (
		'debug_toolbar',
	)
	MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware',)
	DEBUG_TOOLBAR_PANELS = [
		'debug_toolbar.panels.logging.LoggingPanel',
		'debug_toolbar.panels.request.RequestPanel',
		'debug_toolbar.panels.templates.TemplatesPanel',
		'debug_toolbar.panels.sql.SQLPanel',
		'ddt_request_history.panels.request_history.RequestHistoryPanel',
		'debug_toolbar.panels.redirects.RedirectsPanel',
	]
	DEBUG_TOOLBAR_CONFIG = {
		"JQUERY_URL": "/static/js/jquery.min.js",
		"SHOW_COLLAPSED": True,
		"SHOW_TOOLBAR_CALLBACK": "ddt_request_history.panels.request_history.allow_ajax",
		"RESULTS_STORE_SIZE": 100,

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
#	System Preference
# ==================================================#
ROOT_URLCONF 					= 'main.urls'
WSGI_APPLICATION 					= 'main.wsgi.application'
LANGUAGE_CODE 					= 'en-us'
SECRET_KEY 						= 't1n$sjb$ql8pxcx$k!ewrbjy33+=kjsa*cn3pzqfy_iw*xt^t@'

