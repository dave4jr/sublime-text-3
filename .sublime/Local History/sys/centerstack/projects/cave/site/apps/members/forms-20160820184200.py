#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Member
from .models import Level
from .models import Plan
from .models import ReferralSource
from .models import Certification
import django_filters

STATUS_CHOICES = (("", "Status (All)"), ("Active", "Active"), ("Inactive", "Inactive"), ("Terminated", "Terminated"))


#	Django Filters
# ====================================== #
class MemberFilter(django_filters.FilterSet):
	status = django_filters.ChoiceFilter(choices=STATUS_CHOICES)
	class Meta:
		model = Member
		fields = ['status']


class MemberForm(forms.ModelForm):
	referral_source = forms.ModelChoiceField(queryset=ReferralSource.objects.all(), empty_label="Referral Source", required=False)
	level = forms.ModelChoiceField(queryset=Level.objects.all(), empty_label="Level", required=False)
	plan = forms.ModelChoiceField(queryset=Plan.objects.all(), empty_label="Plan", required=False)
	class Meta:
		model = Member
		fields = '__all__'


class LevelForm(forms.ModelForm):
	class Meta:
		model = Level
		fields = '__all__'


class ReferralSourceForm(forms.ModelForm):
	class Meta:
		model = ReferralSource
		fields = '__all__'


class CertificationForm(forms.ModelForm):
	class Meta:
		model = Certification
		fields = '__all__'








