#*======================= #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Class Form
#*======================= #
from django import forms
from .models import Class
from tinymce.widgets import TinyMCE

class ClassForm(forms.ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
	class Meta:
		model = Class
		fields = '__all__'






