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
BEDROOM_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5+"))
BATHROOM_CHOICES = ((0, "1"), (1, "1.5"), (2, "2"), (3, "2.5"), (4, "3"), (5, "3.5"), (6, "4+"))
SQFT_CHOICES = ((0, "< 1,000"), (1, "1,000 - 2,000"), (2, "2,000 - 3,000"), (3, "3,000 - 4,000"), (4, "4,000 - 5,000"), (5, "> 5,000"))
ACRES_CHOICES = ((0, "< 1"), (1, "1 - 5"), (2, "5 - 10"), (3, "10 - 20"), (4, "> 20"))

try:
	city = [('','---------')] + list(Property.objects.values_list('city','city').order_by('city').distinct())
	bedrooms = [('','---------')] + list(Property.objects.values_list('bedrooms','bedrooms').order_by('bedrooms').distinct())
	bathrooms = [('','---------')] + list(Property.objects.values_list('bathrooms','bathrooms').order_by('bathrooms').distinct())
	squarefootage = [('','---------')] + list(Property.objects.values_list('squarefootage','squarefootage').order_by('squarefootage').distinct())
	acres = [('','---------')] + list(Property.objects.values_list('acres','acres').order_by('acres').distinct())
	view = [('','---------')] + list(Property.objects.values_list('view','view').order_by('view').distinct())
	subtype1 = [('','---------')] + list(Property.objects.values_list('subtype1','subtype1').order_by('subtype1').distinct())
	section = [('','---------')] + list(Property.objects.values_list('section','section').order_by('section').distinct())
except:
	city = []
	bedrooms = []
	bathrooms = []
	squarefootage = []
	acres = []
	view = []



#	FilterSet
# ====================================== #
class PropertyFilter(django_filters.FilterSet):

	#	Select
	# ====================================== #
	city = django_filters.ChoiceFilter(choices=city, required=False)
	bedrooms = django_filters.ChoiceFilter(choices=bedrooms, required=False)
	bathrooms = django_filters.ChoiceFilter(choices=bathrooms, required=False)
	view = django_filters.ChoiceFilter(choices=view, required=False)
	subtype1 = django_filters.ChoiceFilter(choices=subtype1, required=False)
	section = django_filters.ChoiceFilter(choices=section, required=False)
	
	#	Sqft Range
	# ====================================== #
	squarefootage = django_filters.NumberFilter(required=False)
	squarefootage__lt = django_filters.NumberFilter(name='squarefootage', lookup_expr='lt', required=False)
	squarefootage__gt = django_filters.NumberFilter(name='squarefootage', lookup_expr='gt', required=False)

	#	Text Range
	# ====================================== #
	listingprice = django_filters.NumberFilter(required=False, localize=True)
	listingprice__lt = django_filters.NumberFilter(name='listingprice', lookup_expr='lt', required=False, localize=True)
	listingprice__gt = django_filters.NumberFilter(name='listingprice', lookup_expr='gt', required=False, localize=True)

	#	Keyword Search
	# ====================================== #
	keysearch = django_filters.CharFilter(lookup_expr='icontains', required=False)

	class Meta:
		model = Property
		order_by = ['-listingprice']







