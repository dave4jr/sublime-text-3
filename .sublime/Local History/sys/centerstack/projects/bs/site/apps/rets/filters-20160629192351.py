#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import Property
import django_filters


#	Lookup Types
# ====================================== #
django_filters.filters.LOOKUP_TYPES = [
	('', '---------'),
	('exact', 'Is equal to'),
	('not_exact', 'Is not equal to'),
	('lt', 'Lesser than'),
	('gt', 'Greater than'),
	('gte', 'Greater than or equal to'),
	('lte', 'Lesser than or equal to'),
	('startswith', 'Starts with'),
	('endswith', 'Ends with'),
	('contains', 'Contains'),
	('not_contains', 'Does not contain'),
]

STATUS_CHOICES = (
	(0, 'Regular'),
	(1, 'Manager'),
	(2, 'Admin'),
)
BED_CHOICES = ((0, "Any"), (1, "1+"), (2, "2+"), (3, "3+"), (4, "4+"), (5, "5+"))
BATH_CHOICES = (("Any", "Any"), ("1+", "1+"), ("1.5+", "1.5+"), ("1.75+", "1.75+"), ("2+", "2+"), ("3+", "3+"), ("4+", "4+"), ("5+", "5+"))
SQ_FT_CHOICES = (("< 600", "< 600"), ("800", "800"), ("1,000", "1,000"), ("1,200", "1,200"), ("1,400", "1,400"), ("1,600", "1,600"), ("1,800", "1,800"), ("2,000", "2,000"), ("2,250", "2,250"), ("2,500", "2,500"), ("2,750", "2,750"), ("3,000", "3,000"), ("3,500", "3,500"), ("4,000", "4,000"), ("5,000", "5,000"), ("6,000", "6,000"), ("7,000", "7,000"), ("8,000", "8,000"), ("9,000", "9,000"), ("10,000", "10,000"), ("> 10,000", "> 10,000"))



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
	city = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('city', flat=True).order_by('city').distinct())
	county = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('county', flat=True).order_by('county').distinct())
	bedrooms = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('bedrooms', flat=True).order_by('bedrooms').distinct())
	bathrooms = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('bathrooms', flat=True).order_by('bathrooms').distinct())
	squarefootage = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('squarefootage', flat=True).order_by('squarefootage').distinct())
	acres = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('acres', flat=True).order_by('acres').distinct())
	listingprice = django_filters.ModelChoiceFilter(queryset=Property.objects.values_list('listingprice', flat=True).order_by('listingprice').distinct())

	class Meta:
		model = Property
		fields = ['city', 'county', 'bedrooms', 'bathrooms', 'squarefootage', 'acres', 'listingprice']







