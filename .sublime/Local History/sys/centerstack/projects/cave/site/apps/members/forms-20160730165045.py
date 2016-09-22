#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Member
from .models import Level
from .models import ReferralSource
from .models import Expertise
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
	referral_source = forms.ModelChoiceField(queryset=ReferralSource.objects.all(), empty_label="Referral Source")
	level = forms.ModelChoiceField(queryset=Level.objects.all(), empty_label="Level")
	certification = forms.ModelChoiceField(queryset=Certification.objects.all(), empty_label="Certification")
	expertise = forms.ModelChoiceField(queryset=Expertise.objects.all(), empty_label="Expertise")
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


class ExpertiseForm(forms.ModelForm):
	class Meta:
		model = Expertise
		fields = '__all__'






