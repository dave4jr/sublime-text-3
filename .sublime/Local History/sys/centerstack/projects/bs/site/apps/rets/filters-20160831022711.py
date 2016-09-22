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



#	Choice Method Filter
# ====================================== #
class ChoiceMethodFilter(django_filters.MethodFilter):
	field_class = forms.ChoiceField


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
	VIEW_CHOICES = (("mountain", "Mountain View"), ("lake", "Lake View"), ("river", "River View"), ("riverfront", "Riverfront"), ("golf", "Golf Course"))
	view = ChoiceMethodFilter(widget=forms.Select, choices=VIEW_CHOICES)
	def filter_view(self, queryset, value):
		return queryset.filter(view__icontains=value)
	
	
	#	Price
	# ====================================== #
	price = django_filters.NumberFilter(name='listingprice', required=False, localize=True)
	price__lt = django_filters.NumberFilter(name='listingprice', lookup_expr='lt', required=False, localize=True)
	price__gt = django_filters.NumberFilter(name='listingprice', lookup_expr='gt', required=False, localize=True)
	

	#	Size
	# ====================================== #
	size = django_filters.NumberFilter(name='squarefootage', required=False, localize=True)
	size__lt = django_filters.NumberFilter(name='squarefootage', lookup_expr='lt', required=False, localize=True)
	size__gt = django_filters.NumberFilter(name='squarefootage', lookup_expr='gt', required=False, localize=True)
	
	
	#	Acres
	# ====================================== #
	acres = django_filters.NumberFilter(name="acres", required=False, localize=True)
	acres__lt = django_filters.NumberFilter(name='acres', lookup_expr='lt', required=False, localize=True)
	acres__gt = django_filters.NumberFilter(name='acres', lookup_expr='gt', required=False, localize=True)


	class Meta:
		model = Property
		order_by = ['-listingprice']







