#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	classes/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Class
from .forms import ClassForm
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
def main(request, template):
	classes = Class.objects.all()
	if request.method == "POST":
		form = ClassForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('classes')
	else:
		form = ClassForm()
	return render(request, template, {"classes":classes, "ClassForm": form } )



#	Edit
# ========================= #
def edit(request, template, pk):
	classes = Class.objects.get(pk=pk)
	if request.method == "POST":
		form = ClassForm(request.POST, instance=classes)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Class.objects.get(pk=pk).delete()
				return redirect('classes')
			except:
				form.save()
				return redirect('classes')
	else:
		form = ClassForm(instance=classes)
	return render(request, template, {"class":classes, "ClassForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Class.objects.get(pk=ii).delete()
		del name[:]
		return redirect('classes')







