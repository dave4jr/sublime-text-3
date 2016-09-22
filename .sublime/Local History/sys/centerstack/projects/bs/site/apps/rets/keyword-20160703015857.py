#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 feed.py
#*====================== #
import os, sys, django
sys.path.append('/sys/centerstack/projects/bs/site')
sys.path.append('/sys/centerstack/projects/bs/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
from rets.models import Property


properties = Property.objects.all()
for ii in properties:
	print ii












