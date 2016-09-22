#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 rets/views.py
#*====================== #
import os, sys, json
from django.contrib import messages
from operator import itemgetter
import unicodedata
from django.shortcuts import render, redirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Property
from .forms import PropertyForm



#	Buy
# ====================================== #
def buy(request, template):
	properties = Property.objects.all()
	count = Property.objects.count()
	context = {
		"properties": properties,
		"count": count,
	}
	return render(request, template, context)



#	Buy Single
# ====================================== #
def buy_single(request, template, pk):
	property_single = Property.objects.get(pk=pk)
	context = {
		"property": property_single,
	}
	return render(request, template, context)



#	Listings
# ====================================== #
def listings(request, template):

	JSON = RetsData.objects.get(pk=1)
	js = json.dumps(JSON.json)
	JSON = json.loads(js)

	f = []
	for ii in JSON:
		if ii['ListingAgentFullName'] == "Molly Brundage":
			f.append(ii)

	js = json.dumps(f)
	JSON = json.loads(js)

	context = {
		"jsons": JSON,
	}
	return render(request, template, context)





