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
from django.conf import settings
from xml.etree import ElementTree
from urlparse import urlparse, urljoin
from inventory.models import Inventory
from inventory.forms import InventoryForm
import amazonproduct


#	Config
# ========================= #
# config = {
# 	'access_key': "AKIAIV7UBXGWGXBNGXOQ",
# 	'secret_key': "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",
# 	'associate_tag': "dave4jr-20",
# 	'locale': "us"
# }
# api = amazonproduct.API(cfg=config)
# items = api.item_lookup("079400379979", SearchIndex='All', IdType='UPC')

# for item in items:
# 	try:
# 		print item
# 	except:
# 		pass

http://webservices.amazon.com/onca/xml?
  Service=AWSECommerceService
  &Operation=ItemLookup
  &ResponseGroup=Large
  &SearchIndex=All
  &IdType=UPC
  &ItemId=635753490879
  &AWSAccessKeyId=[Your_AWSAccessKeyID]
  &AssociateTag=[Your_AssociateTag]
  &Timestamp=[YYYY-MM-DDThh:mm:ssZ]
  &Signature=[Request_Signature]










