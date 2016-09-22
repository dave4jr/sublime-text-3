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


class CheckoutBikeForm(forms.ModelForm):
	class Meta:
		model = Bike
		fields = ("current_mileage", "name")


class CheckoutConditionBikeForm(forms.ModelForm):
	class Meta:
		model = Bike
		fields = ("license_plate", "name")









