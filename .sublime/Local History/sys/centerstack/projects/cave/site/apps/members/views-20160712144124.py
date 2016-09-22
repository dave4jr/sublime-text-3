#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	customers/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
def main(request, template):
	customers = Customer.objects.all()
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customers')
	else:
		form = CustomerForm()
	return render(request, template, {"customers":customers, "CustomerForm": form } )



#	Edit
# ========================= #
def edit(request, template, pk):
	customer = Customer.objects.get(pk=pk)
	if request.method == "POST":
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Customer.objects.get(pk=pk).delete()
				return redirect('customers')
			except:
				form.save()
				return redirect('customers')
	else:
		form = CustomerForm(instance=customer)
	return render(request, template, {"customer":customer, "CustomerForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Customer.objects.get(pk=ii).delete()
		del name[:]
		return redirect('customers')
	return render(request, template, {'customer': customer})







