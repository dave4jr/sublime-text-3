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
	ALLOWED_HOSTS = ["www.brundagesmith.com"]
	ADMINS = MANAGERS = [("Dave Luke", "dave@centerstack.io")]



# ==================================================#
#	Paths
# ==================================================#
BASE_DIR 							= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT	 					= os.path.join(BASE_DIR, 'static', 'media')
STATIC_ROOT	 					= os.path.join(BASE_DIR, 'static', 'static_root')
STATIC_URL 						= '/static/'
MEDIA_URL	 						= '/media/'
SITE_ID							= 1


# ==================================================#
#	Date and Time Settings / Locale Settings
# ==================================================#
TIME_ZONE 						= 'America/Los_Angeles'
TIME_FORMAT						= 'g:i A'
DATE_FORMAT		 				= 'N j, Y'
DATETIME_FORMAT					= 'N j, Y | g:iA'

TIME_INPUT_FORMATS 				= ('%I:%M %p',)
DATE_INPUT_FORMATS 				= ('%m/%d/%Y', '%b %d, %Y', '%Y-%m-%d')
DATETIME_INPUT_FORMATS				= ('%m/%d/%Y, %I:%M %p', '%m/%d/%Y - %I:%M%p', '%m/%d/%Y, %I:%M%p', '%Y-%m-%d %I:%M%p', '%Y-%m-%d %H:%M:%S')

USE_I18N 							= False
USE_L10N 							= True
USE_TZ 							= False

USE_THOUSAND_SEPARATOR			= True
NUMBER_GROUPING					= 3


# ==================================================#
#	Directories
# ==================================================#
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static', 'static_dirs'),
	os.path.join(BASE_DIR, 'apps', 'sudo', 'static', 'static_dirs'),
)
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
			os.path.join(BASE_DIR, 'apps', 'sudo', 'templates'),
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
	'rets',
	'sudo',
	'contact',
	'partners',
	'widget_tweaks',
	'colorfield',
	'mathfilters',
	'django_extensions',
	'annoying',
	'el_pagination',
	'django_filters',
	'django_cron',
	'import_export',
)


# ==================================================#
#	Application Settings
# ==================================================#
EL_PAGINATION_DEFAULT_CALLABLE_EXTREMES = 0
EL_PAGINATION_DEFAULT_CALLABLE_AROUNDS = 2
EL_PAGINATION_DEFAULT_CALLABLE_ARROWS = True
FILTERS_HELP_TEXT_FILTER = False
CRON_CLASSES = [
	"rets.cron.PropertyCron",
]



# ==================================================#
#	System Preferences
# ==================================================#
ROOT_URLCONF 					= 'main.urls'
WSGI_APPLICATION 					= 'main.wsgi.application'
LANGUAGE_CODE 					= 'en-us'
SECRET_KEY 						= 't1n$sjb$ql8pxcx$k!ewrbjy33+=kjsa*cn3pzqfy_iw*xt^t@'

