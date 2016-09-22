#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/views.py
#*========================== #
import logging, sys
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Parnter
from .forms import ParnterForm


def main(request, template):
	contacts = Parnter.objects.all()

	if request.method == "POST":
		form = ParnterForm(request.POST)
	else:
		form = ParnterForm()

	if form.is_valid():
		form.save()
		messages.success(request, "We will get back to you as soon as possible. Thank you!")

	context = {
		"contacts": contacts,
		"ParnterForm": form
	}
	return render(request, template, context)





