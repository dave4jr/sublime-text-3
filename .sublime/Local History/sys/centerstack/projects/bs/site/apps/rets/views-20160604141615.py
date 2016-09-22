#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 rets/views.py
#*====================== #
import os, sys, json
from django.contrib import messages
from django.shortcuts import render, redirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import RetsData



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
# def buy_single(request, template, listing_rid):
	
# 	context = {}
# 	return render(request, template, context)

