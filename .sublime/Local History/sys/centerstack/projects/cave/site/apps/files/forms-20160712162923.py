#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Files Form
#*============================ #
from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = '__all__'
	





