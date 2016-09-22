#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/views.py
#*======================== #
import os, sys, django, requests, re, json, logging, bs4, urllib, urllib2
from django.conf import settings
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Inventory
from .forms import InventoryForm


#	Main
# ========================= #
def main(request, template):
	inventories = Inventory.objects.all()
	if request.method == "POST":
		form = InventoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('inventory')
	else:
		form = InventoryForm()
	return render(request, template, {"inventories":inventories, "InventoryForm": form } )



#	Edit
# ========================= #
def edit(request, template, pk):
	inventory = Inventory.objects.get(pk=pk)
	if request.method == "POST":
		form = InventoryForm(request.POST, instance=inventory)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Inventory.objects.get(pk=pk).delete()
				return redirect('inventory')
			except:
				form.save()
				return redirect('inventory')
	else:
		form = InventoryForm(instance=inventory)
	return render(request, template, {"inventory":inventory, "InventoryForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Inventory.objects.get(pk=ii).delete()
		del name[:]
		return redirect('inventory')



#	UPC Data
# ====================================== #
def upc_data(request, template, upc):
	try:
		request = urllib2.Request("https://api.upcitemdb.com/prod/trial/lookup?upc=%s" % UPC, None, {'User-Agent':'Mozilla/5.0'})
		response = urllib2.urlopen(request).read()
		JSON = json.load(urllib2.urlopen(url))
		data = JSON["items"][0]
	except:
		redirect("index")

	if request.method == "POST":
		form = InventoryForm(request.POST, instance=inventory)
		if form.is_valid():
			inventory = form.save(commit=False)
			inventory.title = data["title"]
			inventory.description = data["description"]
			inventory.save()
			redirect("inventory")
	else:
		form = InventoryForm(instance=inventory)
	return render(request, template, {"InventoryForm": form } )









