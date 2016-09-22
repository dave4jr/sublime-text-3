#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/views.py
#*========================== #
from django.shortcuts import render, redirect
from .models import Charge
from .forms import ChargeForm
 

def charge(request, template):


	context = {

	}
	return render(request, template, context)

