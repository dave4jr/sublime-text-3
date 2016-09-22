#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	gui/forms.py
#*============================ #
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'


