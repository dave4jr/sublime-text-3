#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	calendars/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Calendar
from .forms import CalendarForm
from reservations.models import Reservation
from bikes.models import Bike
from tours.models import Tour
from classes.models import Class
from preferences.models import Preference
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
def main(request, template):
	events = Calendar.objects.all()
	reservations = Reservation.objects.all()
	bikes = Bike.objects.all()
	tours = Tour.objects.all()
	classes = Class.objects.all()
	
	if request.method == "POST":
		form = CalendarForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('calendar')
	else:
		form = CalendarForm()
		
	context = {
			"events":events,
			"reservations":reservations,
			"bikes":bikes,
			"tours":tours,
			"classes":classes,
		}
	return render(request, template, context)



#	Edit
# ========================= #
def edit(request, template, pk):
	event = Calendar.objects.get(pk=pk)
	if request.method == "POST":
		form = CalendarForm(request.POST, instance=event)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Calendar.objects.get(pk=pk).delete()
				return redirect('calendar')
			except:
				form.save()
				return redirect('calendar')
	else:
		form = CalendarForm(instance=event)
	return render(request, template, { "event": event, "CalendarForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Calendar.objects.get(pk=ii).delete()
		del name[:]
		return redirect('calendar')







