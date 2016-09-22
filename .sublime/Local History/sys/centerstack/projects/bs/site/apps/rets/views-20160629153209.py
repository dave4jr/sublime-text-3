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
from .filters import PropertyFilter



#	Buy
# ====================================== #
def buy(request, template):
	property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
	context = {
		"PropertyFilter": property_filter,
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






