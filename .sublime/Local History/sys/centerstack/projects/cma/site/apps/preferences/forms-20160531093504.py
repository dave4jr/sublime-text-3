#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Reservation ModalForm
#*============================ #
from django import forms
from .models import Preferences
from django.forms.widgets import CheckboxSelectMultiple


class PreferencesForm(forms.ModelForm):
	class Meta:
		model = Preferences
		fields = "__all__"
		
		







