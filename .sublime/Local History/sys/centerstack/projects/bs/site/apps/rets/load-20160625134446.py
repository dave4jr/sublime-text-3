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


data = RetsData.objects.get(pk=1)
JSON = data.json

for ii in JSON:
	print ii["ListingRid"]













