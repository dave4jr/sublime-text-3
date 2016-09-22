#*======================= #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Class Form
#*======================= #
from django import forms
from .models import Class

class ClassForm(forms.ModelForm):
	class Meta:
		model = Class
		fields = '__all__'






