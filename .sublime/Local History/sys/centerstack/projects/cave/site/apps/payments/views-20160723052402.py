#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/views.py
#*========================== #
from django.shortcuts import render, redirect, HttpResponse
from django.template import RequestContext
from .models import Payment
from .forms import PaymentForm
 

def charge(request, template):
	if request.method == "POST":
		form = PaymentForm(request.POST)
		if form.is_valid():
			return HttpResponse("Success! We've charged your card!")
	else:
		form = PaymentForm()

	context = {
		"PaymentForm": form,
	}
	return render(request, template, context)
