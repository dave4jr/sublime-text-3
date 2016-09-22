import os
import sys

path = '/home/dave4jr/cave'
path_apps = '/home/dave4jr/cave/apps'

if path not in sys.path:
    sys.path.append(path)
if path_apps not in sys.path:
    sys.path.append(path_apps)

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())