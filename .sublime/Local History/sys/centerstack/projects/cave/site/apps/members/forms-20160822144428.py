#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Member
from .models import Plan
from .models import ReferralSource
from .models import Badge
import django_filters

STATUS_CHOICES = (("", "Status (All)"), ("Active", "Active"), ("Inactive", "Inactive"), ("Terminated", "Terminated"))


#	Django Filters
# ====================================== #
class MemberFilter(django_filters.FilterSet):
	status = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
	class Meta:
		model = Member
		fields = ['status']
		


# class BadgeModelChoiceField(forms.ModelChoiceField):
# 	def label_from_instance(self, obj):
# 		return obj.name



class MemberForm(forms.ModelForm):
	referral_source = forms.ModelChoiceField(queryset=ReferralSource.objects.all(), empty_label="Referral Source", required=False)
	plan = forms.ModelChoiceField(queryset=Plan.objects.all(), empty_label="Plan", required=False)
	badge = forms.ModelMultipleChoiceField(queryset=Badge.objects.all(), required=False)
	class Meta:
		model = Member
		fields = '__all__'



class ReferralSourceForm(forms.ModelForm):
	class Meta:
		model = ReferralSource
		fields = '__all__'


class BadgeForm(forms.ModelForm):
	class Meta:
		model = Badge
		fields = '__all__'








