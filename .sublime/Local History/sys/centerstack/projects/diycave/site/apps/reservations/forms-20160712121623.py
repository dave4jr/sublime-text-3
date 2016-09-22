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
from django.forms.widgets import CheckboxSelectMultiple



# ==================================================#
#	Reservation Form
# ==================================================#
class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"
		widgets = {
			'accessories': forms.CheckboxSelectMultiple(),
		}



# ==================================================#
#	Launch Checkout / Checkin Forms
# ==================================================#
class ProcessingModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return obj.name


class CheckoutLaunchForm(forms.ModelForm):
	customer = ProcessingModelChoiceField(queryset=None)

	def __init__(self, *args, **kwargs):
	        super(CheckoutLaunchForm, self).__init__(*args, **kwargs)
		customer_ids = Reservation.objects.filter(status__exact="reserved").values_list('customer_id', flat=True)
	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
	
	class Meta:
		fields = ("customer",)
		model = Reservation


class CheckinLaunchForm(forms.ModelForm):
	customer = ProcessingModelChoiceField(queryset=None)
	
	def __init__(self, *args, **kwargs):
	        super(CheckinLaunchForm, self).__init__(*args, **kwargs)
		customer_ids = Reservation.objects.filter(status__exact="checked_out").values_list('customer_id', flat=True)
	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
	
	class Meta:
		fields = ("customer",)
		model = Reservation


# ==================================================#
#	Checkout / Checkin Forms
# ==================================================#
class CheckoutForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"

class CheckinForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"


class CheckoutConditionForm(forms.ModelForm):
	class Meta:
		model = Reservation
		exclude = ("status",)

class CheckoutMembershipForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"

class CheckoutLiabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"




# ==================================================#
#	Availability Form
# ==================================================#
class AvailabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"


		






