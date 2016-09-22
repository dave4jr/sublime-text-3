#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import Property



class PropertyForm(forms.ModelForm):
	city = forms.ModelChoiceField(queryset=Property.objects.values_list('city', flat=True).order_by('city').distinct())
	county = forms.ModelChoiceField(queryset=Property.objects.values_list('county', flat=True).order_by('county').distinct())
	bedrooms = forms.ModelChoiceField(queryset=Property.objects.values_list('bedrooms', flat=True).order_by('bedrooms').distinct())
	bathrooms = forms.ModelChoiceField(queryset=Property.objects.values_list('bathrooms', flat=True).order_by('bathrooms').distinct())
	squarefootage = forms.ModelChoiceField(queryset=Property.objects.values_list('squarefootage', flat=True).order_by('squarefootage').distinct())
	acres = forms.ModelChoiceField(queryset=Property.objects.values_list('acres', flat=True).order_by('acres').distinct())
	listingprice = forms.ModelChoiceField(queryset=Property.objects.values_list('listingprice', flat=True).order_by('listingprice').distinct())
	
	class Meta:
		model = Property
		fields = '__all__'




#	Property Filters
# ====================================== #
# class PropertyForm(forms.ModelForm):
# 	customer = CustomModelChoiceField(queryset=None)
# 	bike = CustomModelChoiceField(queryset=None)
	

# 	def __init__(self, *args, **kwargs):
# 	        super(PropertyForm, self).__init__(*args, **kwargs)
# 		customer_ids = Reservation.objects.filter(status__exact="reserved").values_list('customer_id', flat=True)
# 		bike_ids = Reservation.objects.filter(status__exact="reserved").values_list('bike_id', flat=True)

# 	        self.fields['customer'].queryset = Customer.objects.filter(id__in=customer_ids)
# 	        self.fields['bike'].queryset = Bike.objects.filter(id__in=bike_ids)
	
# 	class Meta:
# 		fields = "__all__"
# 		model = Reservation
