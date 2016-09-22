#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	blog/forms.py
#*============================ #
from django import forms
from .models import Blog
from django.conf import settings
from django.utils.safestring import mark_safe



class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = '__all__'


