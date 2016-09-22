#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/views.py
#*======================== #
import os, sys, django, requests, re, json, logging, bs4
sys.path.append('/sys/centerstack/projects/cave/site')
sys.path.append('/sys/centerstack/projects/cave/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
from django.shortcuts import render, redirect
import urllib2, urllib
from django.conf import settings
from xml.etree import ElementTree
from urlparse import urlparse, urljoin
from inventory.models import Inventory
from inventory.forms import InventoryForm
import amazonproduct

UPC = "079400379979"

url = "https://api.upcitemdb.com/prod/trial/lookup?upc=%s" % UPC
user_agent = {'User-Agent':'Mozilla/5.0'}
request = urllib2.Request(url, None, user_agent)
response = urllib2.urlopen(request).read()
JSON = json.load(urllib2.urlopen(url))
data = JSON["items"][0]
print data["upc"]
# for ii in data:
# 	print ii

# for key, value in JSON.items.iteritems():
# 	print key, value
# soup = bs4.BeautifulSoup(response, "lxml")
# print soup.p.text.find("items")
# soup = bs4.BeautifulSoup(response, "lxml")
# print soup.prettify()



