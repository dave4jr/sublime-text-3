#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Bike ModalForm
#*============================ #
from django import forms
from .models import Bike

class BikeForm(forms.ModelForm):
	class Meta:
		model = Bike
		fields = '__all__'









