#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	profiles/views.py
#*======================== #
from django.shortcuts import render, redirect
import logging, sys
from .models import UserProfile
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
def main(request, template):
	context = {}
	return render(request, template, context )






