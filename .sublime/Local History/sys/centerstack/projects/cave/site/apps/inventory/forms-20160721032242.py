#*======================= #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Inventory Form
#*======================= #
from django import forms
from .models import Inventory
from tinymce.widgets import TinyMCE

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = '__all__'






