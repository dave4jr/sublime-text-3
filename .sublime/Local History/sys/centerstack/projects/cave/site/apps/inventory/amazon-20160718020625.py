#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.conf import settings
import logging, sys
from .models import Inventory
from .forms import InventoryForm
import amazonproduct


#	Config
# ========================= #
config = {
	'access_key': settings.AWS_ACCESS_KEY,
	'secret_key': settings.AWS_SECRET_ACCESS_KEY,
	'associate_tag': settings.AWS_ASSOCIATE_TAG,
	'locale': settins.AWS_LOCALE
}
api = amazonproduct.API(cfg=config)
items = api.item_search('Books', Publisher="O'Reilly")

for item in items:
	print item











