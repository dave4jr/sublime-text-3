#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	profiles/views.py
#*======================== #
from django.shortcuts import render, redirect
import logging, sys
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required



def main(request, template):
	users = UserProfile.objects.all()

	if request.method == 'POST':
		form = UserProfileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('users')
	else:
		form = UserProfileForm(request.FILES)

	context = {
		"users": users,
		"form": form,
	}
	return render(request, template, context)





