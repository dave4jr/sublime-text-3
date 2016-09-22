#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 load.py
#*====================== #
import os, sys, django
sys.path.append('/sys/centerstack/projects/bs/site')
sys.path.append('/sys/centerstack/projects/bs/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
import sys, bs4, re, json
from django.core import serializers
from pprint import pprint as pp
from rets.models import RetsData
from rets.models import Property


#	Rets JSON
# ====================================== #
data = RetsData.objects.get(pk=1)
JSON = data.json


#	Assigning JSON Fields to Model Fields
# ====================================== #
kk = 1
for house in JSON:
	defaults = {}
	for key, value in house.iteritems():
		defaults[key.lower()] = value
	unit, created = Property.objects.update_or_create(property_id=str(kk), defaults=defaults)
	unit.save()
	kk += 1


	













