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



#	Main
# ====================================== #
def main(request, template):
	context = {}
	return render(request, template, context)





#	Admin
# ====================================== #
def admin(request):
	context = {}
	return render(request, context)


