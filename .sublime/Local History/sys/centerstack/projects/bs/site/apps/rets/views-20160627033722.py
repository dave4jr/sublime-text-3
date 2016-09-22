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
	try:
		page = request.GET.get('page', 1)
	except PageNotAnInteger:
		page = 1

	properties = Property.objects.all()
	if request.method == "POST":
		form = PropertyForm(request.POST, instance=properties)
		if form.is_valid():
			form.save()
			return redirect('buy')
	else:
		form = PropertyForm()

	p = Paginator(properties, per_page=15)
	context = {
		"properties": p.page(page),
		"count": Property.objects.count(),
		"BuyForm": form,
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

	listings = Property.objects.filter(listingagentfullname="Molly Brundage")
	count = Property.objects.filter(listingagentfullname="Molly Brundage").count()

	context = {
		"properties": listings,
		"count": count,
	}
	return render(request, template, context)






