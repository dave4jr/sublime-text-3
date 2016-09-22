#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Bike
from .forms import BikeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max


#	Main
# ========================= #
def main(request, template):
	inventory = Bike.objects.all()
	count = Bike.objects.all().count()

	if count == 0:
		max_mileage = 0
	else:
		try:
			max_mileage = Bike.objects.all().aggregate(Max('current_mileage'))['current_mileage__max'] + 5000
		except:
			max_mileage = 0
	

	if request.method == "POST":
		form = BikeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('inventory')
	else:
		form = BikeForm()
	return render(request, template, {"inventory":inventory, "BikeForm": form, "mileage_max": max_mileage } )



#	Edit
# ========================= #
def edit(request, template, pk):
	bike = Bike.objects.get(pk=pk)
	if request.method == "POST":
		form = BikeForm(request.POST, request.FILES, instance=bike)
		if form.is_valid():
			try:
				action = list(request.POST.getlist('delete'))[0]
				Bike.objects.get(pk=pk).delete()
				logging.debug("Delete")
				return redirect('inventory')
			except:
				form.save()
				return redirect('inventory')
	else:
		form = BikeForm(instance=bike)
	return render(request, template, {"bike":bike, "BikeForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Bike.objects.get(pk=ii).delete()
		del name[:]
		return redirect('inventory')
	return render(request, template, {'bike': bike})







