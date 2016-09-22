#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import Property
import django_filters


#	Choices
# ====================================== #
city = Property.objects.values_list('city', 'city').order_by('city').distinct()
county = Property.objects.values_list('county', 'county').order_by('county').distinct()
bedrooms = Property.objects.values_list('bedrooms', 'bedrooms').order_by('bedrooms').distinct()
bathrooms = Property.objects.values_list('bathrooms', 'bathrooms').order_by('bathrooms').distinct()
squarefootage = Property.objects.values_list('squarefootage', 'squarefootage').order_by('squarefootage').distinct()
acres = Property.objects.values_list('acres', 'acres').order_by('acres').distinct()
listingprice = Property.objects.values_list('listingprice', 'listingprice').order_by('listingprice').distinct()


#	Filter (GET)
# ====================================== #
class PropertyFilter(django_filters.FilterSet):
	city = django_filters.ChoiceFilter(choices=city)

	class Meta:
		model = Property
		fields = ['city', 'county', 'bedrooms', 'bathrooms', 'squarefootage', 'acres', 'listingprice']




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





