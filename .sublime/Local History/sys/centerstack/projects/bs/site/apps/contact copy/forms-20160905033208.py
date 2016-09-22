#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	partners/forms.py
#*============================ #
from django import forms
from .models import Partner


class PartnerForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = '__all__'


