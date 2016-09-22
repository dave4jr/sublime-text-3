#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	gui/forms.py
#*============================ #
from django import forms
from .models import Contact
from django.conf import settings
from django.utils.safestring import mark_safe



class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'


