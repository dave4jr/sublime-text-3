#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	blog/views.py
#*========================== #
import logging, sys
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog


def main(request, template):
	blogs = Blog.objects.all()
	context = {
		"blogs": blogs,
	}
	return render(request, template, context)


def single(request, template, pk):
	blog = Blog.objects.get(pk=pk)
	context = {
		"blog": blog,
	}
	return render(request, template, context)








