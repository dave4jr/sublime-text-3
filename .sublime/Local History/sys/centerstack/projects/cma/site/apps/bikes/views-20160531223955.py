#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	bikes/views.py
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
	bikes = Bike.objects.all()
	count = Bike.objects.all().count()

	if count == 0:
		max_milage = 0
	else:
		max_milage = Bike.objects.all().aggregate(Max('current_milage'))['current_milage__max'] + 5000
	

	if request.method == "POST":
		form = BikeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('bikes')
	else:
		form = BikeForm()
	return render(request, template, {"bikes":bikes, "BikeForm": form, "milage_max": max_milage } )



#	Edit
# ========================= #
def edit(request, template, pk):
	bike = Bike.objects.get(pk=pk)
	if request.method == "POST":
		form = BikeForm(request.POST, instance=bike)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Bike.objects.get(pk=pk).delete()
				return redirect('bikes')
			except:
				form.save()
				return redirect('bikes')
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
		return redirect('bikes')
	return render(request, template, {'bike': bike})







