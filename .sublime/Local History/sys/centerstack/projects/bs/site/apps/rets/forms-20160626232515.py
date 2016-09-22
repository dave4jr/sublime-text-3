#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = '__all__'



