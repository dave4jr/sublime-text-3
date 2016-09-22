#*======================= #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Calendar Form
#*======================= #
from django import forms
from .models import Calendar

class CalendarForm(forms.ModelForm):
	class Meta:
		model = Calendar
		fields = '__all__'





