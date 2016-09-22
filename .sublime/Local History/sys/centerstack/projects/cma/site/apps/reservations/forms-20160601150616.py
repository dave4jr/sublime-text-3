#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Reservation ModalForm
#*============================ #
from django import forms
from .models import Reservation
from customers.models import Customer
from bikes.models import Bike
from multiupload.fields import MultiFileField
from django.forms.widgets import CheckboxSelectMultiple


#	Reservation Form
# ====================================== #
class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"
		widgets = {
			'bike_accessories': forms.CheckboxSelectMultiple(),
			'storage_accessories': forms.CheckboxSelectMultiple(),
			'tour_accessories': forms.CheckboxSelectMultiple()
		}



#	CustomModelChoiceField Customization
# ====================================== #
class CustomModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


#	Checkout
# ====================================== #
class CheckoutForm(forms.ModelForm):
	customer = CustomModelChoiceField(queryset=None)
	bike = CustomModelChoiceField(queryset=None)
	

	def __init__(self, *args, **kwargs):
	        super(CheckoutForm, self).__init__(*args, **kwargs)
		customer_ids = Reservation.objects.filter(status__exact="reserved").values_list('customer_id', flat=True)
		bike_ids = Reservation.objects.filter(status__exact="reserved").values_list('bike_id', flat=True)

	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
	        self.fields['bike'].queryset = Bike.objects.filter(id__in=bike_ids)
	
	class Meta:
		fields = "__all__"
		model = Reservation


#	Checkin
# ====================================== #
class CheckinForm(forms.ModelForm):
	customer = CustomModelChoiceField(queryset=None)
	bike = CustomModelChoiceField(queryset=None)
	

	def __init__(self, *args, **kwargs):
	        super(CheckinForm, self).__init__(*args, **kwargs)
		customer_ids = Reservation.objects.filter(status__exact="checked_out").values_list('customer_id', flat=True)
		bike_ids = Reservation.objects.filter(status__exact="checked_out").values_list('bike_id', flat=True)

	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
	        self.fields['bike'].queryset = Bike.objects.filter(id__in=bike_ids)
	
	class Meta:
		fields = "__all__"
		model = Reservation







#	Search Availability
# ====================================== #
class AvailabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"


		





