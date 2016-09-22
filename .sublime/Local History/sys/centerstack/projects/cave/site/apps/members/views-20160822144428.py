#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		DIYcave
#*  Description:	members/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.http import HttpResponse, QueryDict
from django.template.loader import render_to_string
from django.core import serializers
from django.conf import settings
import logging, sys, json
from .models import Member
from .forms import MemberForm
from .forms import MemberFilter
from django.contrib.auth.decorators import login_required





#	Main
# ========================= #
def main(request, template):
	members = MemberFilter(request.GET, queryset=Member.objects.all())

	if request.method == "POST":
		action = request.POST.get("action","")
		if action == "save":
			ajax_form = QueryDict(request.POST.get("form",""))
			form = MemberForm(ajax_form)
			if form.is_valid():
				form.save()
				return redirect('members')
		elif action == "delete":
			return redirect('members')
		else:
			return redirect('members')
	else:
		form = MemberForm()
		
	return render(request, template, {"members":members, "MemberForm": form } )


	

	
#	Edit
# ========================= #
def edit(request, template, pk):
	member = Member.objects.get(pk=pk)
	
	action = request.POST.get("action","")
	if action == "save":
		ajax_form = QueryDict(request.POST.get("form",""))
		form = MemberForm(ajax_form, instance=member)
		if form.is_valid():
			form.save()
			return redirect('members')
	else:
		form = MemberForm(instance=member)
	
	return render(request, template, {"member":member, "MemberForm": form } )











#	Ajax Submit Member
# ====================================== #
def populate_table(request):
	members = MemberFilter(request.GET, queryset=Member.objects.all())
	JSON = serializers.serialize('json', members)
	
	return HttpResponse(JSON, content_type='application/json')
		
















# def main(request, template):
# 	members = MemberFilter(request.GET, queryset=Member.objects.all())
# 	if request.method == "POST":
# 		form = MemberForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('members')
# 	else:
# 		form = MemberForm()
# 	return render(request, template, {"members":members, "MemberForm": form } )







# #	Delete
# # ========================= #
# value = []
# def delete(request, template):
# 	if request.method == "POST":
# 		name = list(request.POST.getlist('checked'))
# 		for ii in name:
# 			Member.objects.get(pk=ii).delete()
# 		del name[:]
# 		return redirect('members')
# 	return render(request, template, {'member': member})







