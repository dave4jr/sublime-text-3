#*======================= #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Inventory Form
#*======================= #
from django import forms
from .models import Inventory
from tinymce.widgets import TinyMCE

class InventoryForm(forms.ModelForm):
	# description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
	class Meta:
		model = Inventory
		fields = '__all__'






