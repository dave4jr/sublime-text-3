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
from .forms import PropertyFilter



#	Buy
# ====================================== #
def buy(request, template):
	property_filter = PropertyFilter(request.GET, queryset=Property.objects.all())
	context = {
		"PropertyFilter": property_filter,
	}
	return render(request, template, context)


# def buy(request, template):
# 	try:
# 		page = request.GET.get('page', 1)
# 	except PageNotAnInteger:
# 		page = 1

# 	if request.method == "POST":
# 		form = PropertyForm(request.POST)

# 		city = request.POST.getlist('city')[0]
# 		print city
# 		county = request.POST.getlist('county')[0]
# 		bedrooms = request.POST.getlist('bedrooms')[0]
# 		bathrooms = request.POST.getlist('bathrooms')[0]
# 		squarefootage = request.POST.getlist('squarefootage')[0]
# 		acres = request.POST.getlist('acres')[0]
# 		listingprice = request.POST.getlist('listingprice')[0]
		
# 		properties = Property.objects.filter(city=city, county=county, bedrooms=bedrooms, bathrooms=bathrooms, squarefootage=squarefootage, acres=acres, listingprice=listingprice)
# 		property_count = Property.objects.filter(city=city, county=county, bedrooms=bedrooms, bathrooms=bathrooms, squarefootage=squarefootage, acres=acres, listingprice=listingprice).count()
		
# 		p = Paginator(properties, per_page=15)
# 		properties = p.page(page)

# 	else:
# 		form = PropertyForm()
# 		properties = 0
# 		property_count = 0

# 	context = {
# 		"properties": properties,
# 		"count": property_count,
# 		"PropertyForm": form,
# 	}
# 	return render(request, template, context)



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



		# Poll.objects.get(
		#     Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
		#     question__startswith='Who',
		# )




