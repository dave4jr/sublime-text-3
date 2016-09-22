#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	wsgi.py
#*========================== #
import os
import sys

path = '/home/dave4jr/bond6'
path_apps = '/home/dave4jr/bond6/apps'

if path not in sys.path:
    sys.path.append(path)
if path_apps not in sys.path:
    sys.path.append(path_apps)

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
