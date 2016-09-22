#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	customs/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Custom
from .forms import CustomForm
from django.contrib.auth.decorators import login_required


#	Main / New
# ========================= #
def main(request, template):
	customs = Custom.objects.all()
	if request.method == "POST":
		form = CustomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('custom')
	else:
		form = CustomForm()
	return render(request, template, {"customs":customs, "CustomForm": form } )


#	Edit
# ========================= #
def edit(request, template, pk):
	custom = Custom.objects.get(pk=pk)
	if request.method == "POST":
		form = CustomForm(request.POST, instance=custom)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Custom.objects.get(pk=pk).delete()
				return redirect('custom')
			except:
				form.save()
				return redirect('custom')
	else:
		form = CustomForm(instance=custom)
	return render(request, template, {"custom":custom, "CustomForm": form } )


#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Custom.objects.get(pk=ii).delete()
		del name[:]
		return redirect('custom')
	return render(request, template, {'custom': custom})







