#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 rets/views.py
#*====================== #
import os, sys, json
from django.contrib import messages
import unicodedata
from django.shortcuts import render, redirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import RetsData



#	Buy
# ====================================== #
def buy(request, template):
	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	JSON = RetsData.objects.get(pk=1)
	js = json.dumps(JSON.json)
	JSON = json.loads(js)

	p = Paginator(JSON, per_page=6)
	jsons = p.page(page)


	context = {
		"jsons": jsons,
		"page": p,
	}
	return render(request, template, context)



#	Buy Single
# ====================================== #
def buy_single(request, template, listing_rid):

	JSON = RetsData.objects.get(pk=1)
	js = json.dumps(JSON.json)
	JSON = json.loads(js)

	f = {}
	for ii in JSON:
		if ii['ListingRid'] == listing_rid:
			for yy in ii:
				value = ii[yy]
				key = yy
				f[key] = value

	js = json.dumps(f)
	JSON = json.loads(js)

	context = {
		"json": JSON,
	}
	return render(request, template, context)



#	Listings
# ====================================== #
def listings(request, template, listing_rid):

	JSON = RetsData.objects.get(pk=1)
	js = json.dumps(JSON.json)
	JSON = json.loads(js)

	f = {}
	for ii in JSON:
		if ii['ListingRid'] == listing_rid:
			for yy in ii:
				value = ii[yy]
				key = yy
				f[key] = value

	js = json.dumps(f)
	JSON = json.loads(js)

	context = {
		"jsons": JSON,
	}
	return render(request, template, context)




