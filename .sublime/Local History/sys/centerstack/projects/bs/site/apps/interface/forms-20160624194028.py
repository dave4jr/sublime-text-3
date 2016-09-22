#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/forms.py
#*============================ #
from django.utils.safestring import mark_safe
from django.conf import settings
from django import forms
from .models import Contact
from .models import Sell


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'


class SellForm(forms.ModelForm):
	class Meta:
		model = Sell
		fields = '__all__'


