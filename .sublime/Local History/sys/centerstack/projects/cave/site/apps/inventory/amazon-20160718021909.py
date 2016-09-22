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
from inventory.models import Inventory
from inventory.forms import InventoryForm
import amazonproduct


#	Config
# ========================= #
config = {
	'access_key': "AKIAIV7UBXGWGXBNGXOQ",
	'secret_key': "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",
	'associate_tag': "dave4jr-20",
	'locale': "us"
}
api = amazonproduct.API(cfg=config)
items = api.item_search('Books', Publisher="O'Reilly")

for item in items:
	print item.ItemAttributes.Author











