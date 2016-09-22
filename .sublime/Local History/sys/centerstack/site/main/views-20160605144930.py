#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 views.py
#*====================== #
import os, sys
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from newsletter.models import Newsletter
from newsletter.forms import NewsletterForm



APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.basename(APP_DIR)


#	Main
# ====================================== #
def main(request, template):
	newsletters = Newsletter.objects.all()

	if request.method == "POST":
		form = NewsletterForm(request.POST)
	else:
		form = NewsletterForm()

	if form.is_valid():
		form.save()
		messages.success(request, "Thank you for subscribing!")

	context = {
		"newsletters": newsletters,
		"NewsletterForm": form
	}
	return render(request, template, context)


#	Admin
# ====================================== #
def admin(request):
	context = {}
	return render(request, context)


