#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/admin.py
#*============================ #
from django.contrib import admin
from .models import Charge


admin.site.register(Charge)


