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
		model = Reservation
		fields = ("customer",)


class CheckinLaunchForm(forms.ModelForm):
	customer = ProcessingModelChoiceField(queryset=None)
	
	def __init__(self, *args, **kwargs):
	        super(CheckinLaunchForm, self).__init__(*args, **kwargs)
		customer_ids = Reservation.objects.filter(status__exact="checked_out").values_list('customer_id', flat=True)
	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
	
	class Meta:
		model = Reservation
		fields = ("customer",)


# ==================================================#
#	Checkout / Checkin Forms
# ==================================================#
class CheckoutForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ("customer", "checkout_datetime", "notes")

class CheckinForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ("customer", "checkout_datetime", "notes")


class CheckoutConditionForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = ("customer", "checkout_datetime", "checkin_datetime", "checkout_condition_img_1", "checkout_condition_img_2", "checkout_condition_img_3", "checkout_condition_img_4", "checkout_condition_img_5", "checkout_condition_img_6","notes")

class CheckoutMembershipForm(forms.ModelForm):
	class Meta:
		model = Reservation
		exclude = ('status',)

class CheckoutLiabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		exclude = ('status',)




# ==================================================#
#	Availability Form
# ==================================================#
class AvailabilityForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields = "__all__"


		






