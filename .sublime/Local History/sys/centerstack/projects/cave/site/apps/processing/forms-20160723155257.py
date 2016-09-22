#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Processing



class ProcessingForm(forms.ModelForm):
	class Meta:
		model = Processing
		fields = '__all__'







