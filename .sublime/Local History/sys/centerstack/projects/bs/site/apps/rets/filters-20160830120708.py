#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/forms.py
#*============================ #
from django.conf import settings
from django import forms
from .models import Property
import django_filters
from django.forms.widgets import CheckboxSelectMultiple




#	Choices
# ====================================== #
BEDROOM_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5+"))
BATHROOM_CHOICES = ((0, "1"), (1, "1.5"), (2, "2"), (3, "2.5"), (4, "3"), (5, "3.5"), (6, "4+"))
SQFT_CHOICES = ((0, "< 1,000"), (1000, "1,000 - 2,000"), (2000, "2,000 - 3,000"), (3000, "3,000 - 4,000"), (4000, "4,000 - 5,000"), (5000, "> 5,000"))
ACRES_CHOICES = ((0, "< 1"), (1, "1 - 5"), (2, "5 - 10"), (3, "10 - 20"), (4, "> 20"))
VIEW_CHOICES = (("Mountain View", "Mountain View"), ("Lake View", "Lake View"), ("River View", "River View"), ("Riverfront", "Riverfront"), ("Golf Course", "Golf Course"))
PRICE_CHOICES = ((100000, "$100,000"), (150000, "$150,000"), (200000, "$200,000"), (250000, "$250,000"), (300000, "$300,000"), (350000, "$350,000"), (400000, "$400,000"), (450000, "$450,000"), (500000, "$500,000"), (550000, "$550,000"), (600000, "$600,000"), (650000, "$650,000"), (700000, "$700,000"), (750000, "$750,000"), (800000, "$800,000"), (850000, "$850,000"), (900000, "$900,000"), (950000, "$950,000"), (1000000, "$1 Million"), (2000000, "$2 Million"), (3000000, "$3 Million"))


	# Mountain View
	# Lake View
	# River View
	# Riverfront
	# Golf Course



#	FilterSet
# ====================================== #
class PropertyFilter(django_filters.FilterSet):
	
	city = django_filters.MultipleChoiceFilter(choices=Property.objects.values_list('city','city').order_by('city').distinct(), required=False)
	propertytype = django_filters.MultipleChoiceFilter(choices=Property.objects.values_list('propertytype','propertytype').order_by('propertytype').distinct(), required=False)
	section = django_filters.MultipleChoiceFilter(choices=Property.objects.values_list('section','section').order_by('section').distinct(), required=False)
	bedrooms = django_filters.MultipleChoiceFilter(choices=Property.objects.values_list('bedrooms','bedrooms').order_by('bedrooms').distinct(), required=False)
	bathrooms = django_filters.MultipleChoiceFilter(choices=Property.objects.values_list('bathrooms','bathrooms').order_by('bathrooms').distinct(), required=False)
	keysearch = django_filters.CharFilter(lookup_expr='icontains', required=False)
	
	
	#	View
	# ====================================== #
	view = django_filters.MultipleChoiceFilter(choices=VIEW_CHOICES, name="view", required=False)
	
	
	#	Listing Price
	# ====================================== #
	# price = django_filters.MethodFilter(choice=)
	# def range_choice_filter(self, queryset, value):
		
	
	
	# def filter_published(self, queryset, value):
	#         if value:
	#             return queryset.filter(published__isnull=False)
	#         return queryset
	
	
	PRICE_GT_CHOICES = ((200000, "$200,000"), (300000, "$300,000"), (400000, "$400,000"), (500000, "$500,000"), (600000, "$600,000"), (700000, "$700,000"), (800000, "$800,000"), (900000, "$900,000"), (1000000, "$1 Million"), (2000000, "$2 Million"), (3000000, "$3 Million"))
	PRICE_LT_CHOICES = ((300000, "$300,000"), (400000, "$400,000"), (500000, "$500,000"), (600000, "$600,000"), (700000, "$700,000"), (800000, "$800,000"), (900000, "$900,000"), (1000000, "$1 Million"), (2000000, "$2 Million"), (3000000, "$3 Million"),(4000000, "$4 Million"), (5000000, "$5 Million"), (6000000, "$6+ Million"))
	price = django_filters.NumberFilter(name="listingprice", required=False, localize=True)
	price__gt = django_filters.ChoiceFilter(choices=PRICE_GT_CHOICES, name="listingprice", lookup_expr='gt', required=False, localize=True)
	price__lt = django_filters.ChoiceFilter(choices=PRICE_LT_CHOICES, name="listingprice", lookup_expr='lt', required=False, localize=True)
	# price__lt = django_filters.NumberFilter(name='listingprice', lookup_expr='lt', required=False, localize=True)
	# price__gt = django_filters.NumberFilter(name='listingprice', lookup_expr='gt', required=False, localize=True)
	price_range = django_filters.RangeFilter(name="listingprice")
	
	
	#	Lot Size
	# ====================================== #
	acres = django_filters.NumberFilter(required=False, localize=True)
	acres__lt = django_filters.NumberFilter(name='acres', lookup_expr='lt', required=False, localize=True)
	acres__gt = django_filters.NumberFilter(name='acres', lookup_expr='gt', required=False, localize=True)
	

	#	Keyword Search
	# ====================================== #
	squarefootage = django_filters.NumberFilter(required=False)
	squarefootage__lt = django_filters.NumberFilter(name='squarefootage', lookup_expr='lt', required=False)
	squarefootage__gt = django_filters.NumberFilter(name='squarefootage', lookup_expr='gt', required=False)

	class Meta:
		model = Property
		order_by = ['-listingprice']







