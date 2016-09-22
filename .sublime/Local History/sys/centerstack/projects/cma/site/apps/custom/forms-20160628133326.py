#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Tour ModalForm
#*============================ #
from django import forms
from .models import Tour

class TourForm(forms.ModelForm):
	class Meta:
		model = Tour
		fields = '__all__'





