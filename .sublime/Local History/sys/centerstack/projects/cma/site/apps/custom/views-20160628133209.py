#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	tours/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Custom
from django.contrib.auth.decorators import login_required


#	Main / New
# ========================= #
def main(request, template):
	tours = Custom.objects.all()
	if request.method == "POST":
		form = CustomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tours')
	else:
		form = CustomForm()
	return render(request, template, {"tours":tours, "CustomForm": form } )


#	Edit
# ========================= #
def edit(request, template, pk):
	tour = Custom.objects.get(pk=pk)
	if request.method == "POST":
		form = CustomForm(request.POST, instance=tour)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Custom.objects.get(pk=pk).delete()
				return redirect('tours')
			except:
				form.save()
				return redirect('tours')
	else:
		form = CustomForm(instance=tour)
	return render(request, template, {"tour":tour, "CustomForm": form } )


#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Custom.objects.get(pk=ii).delete()
		del name[:]
		return redirect('tours')
	return render(request, template, {'tour': tour})







