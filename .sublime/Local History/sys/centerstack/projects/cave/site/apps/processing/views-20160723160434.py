#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	members/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Processing
from .forms import ProcessingForm
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
# def main(request, template):
# 	members = Member.objects.all()
# 	if request.method == "POST":
# 		form = MemberForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('members')
# 	else:
# 		form = MemberForm()
# 	return render(request, template, {"members":members, "MemberForm": form } )






