#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Reservation ModalForm
#*============================ #
from django import forms
from .models import Preference
from django.forms.widgets import CheckboxSelectMultiple


class PreferenceForm(forms.ModelForm):
	class Meta:
		model = Preference
		fields = "__all__"
		
		







