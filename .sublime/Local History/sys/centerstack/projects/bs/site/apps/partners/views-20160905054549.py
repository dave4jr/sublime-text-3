#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/views.py
#*========================== #
import logging, sys
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Partner
from .forms import PartnerForm


def main(request, template):
	partners = Partner.objects.all()

	if request.method == "POST":
		form = PartnerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('partners')
	else:
		form = PartnerForm()

	context = {
		"partners": partners,
		"PartnerForm": form
	}
	return render(request, template, context)



#	Buy Single
# ====================================== #
def partners_single(request, template, pk):
	partner = Partner.objects.get(pk=pk)
	context = {
		"partner": partner,
	}
	return render(request, template, context)




