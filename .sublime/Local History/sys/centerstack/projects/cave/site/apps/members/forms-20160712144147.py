#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	Member ModalForm
#*============================ #
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = '__all__'






