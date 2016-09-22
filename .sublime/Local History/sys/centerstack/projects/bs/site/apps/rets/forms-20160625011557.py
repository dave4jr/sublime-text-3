#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import RetsData


class RetsDataForm(forms.ModelForm):
	class Meta:
		model = RetsData
		fields = '__all__'



