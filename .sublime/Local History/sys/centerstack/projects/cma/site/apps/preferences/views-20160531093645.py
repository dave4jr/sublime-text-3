#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	preferences/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Preference
from .forms import PreferenceForm
import logging, sys



#	Main
# ========================= #
def main(request, template):
	preference = Preference.objects.get(pk=1)
	if request.method == "POST":
		form = PreferenceForm(request.POST, instance=preference)
		if form.is_valid():
			form.save()
			return redirect('preferences')
	else:
		form = PreferenceForm(instance=preference)
	return render(request, template, {"preference":preference, "PreferenceForm": form } )


