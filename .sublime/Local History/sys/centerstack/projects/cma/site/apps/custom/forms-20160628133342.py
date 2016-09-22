#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Custom ModelForm
#*============================ #
from django import forms
from .models import Custom

class CustomForm(forms.ModelForm):
	class Meta:
		model = Custom
		fields = '__all__'






