#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	members/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.core import serializers
import logging, sys
from .models import Member
from .forms import MemberForm
from .forms import MemberFilter
from django.contrib.auth.decorators import login_required


#	Main
# ========================= #
def main(request, template):
	member_filter = MemberFilter(request.GET, queryset=Member.objects.all())
	if request.method == "POST":
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('members')
	else:
		form = MemberForm()
	return render(request, template, {"MemberFilter":member_filter, "MemberForm": form } )



#	Edit
# ========================= #
def edit(request, template, pk):
	member = Member.objects.get(pk=pk)
	if request.method == "POST":
		form = MemberForm(request.POST, instance=member)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Member.objects.get(pk=pk).delete()
				return redirect('members')
			except:
				form.save()
				return redirect('members')
	else:
		form = MemberForm(instance=member)
	return render(request, template, {"member":member, "MemberForm": form } )



#	Delete
# ========================= #
value = []
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Member.objects.get(pk=ii).delete()
		del name[:]
		return redirect('members')
	return render(request, template, {'member': member})







