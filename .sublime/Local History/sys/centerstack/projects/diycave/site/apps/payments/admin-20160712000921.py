#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/admin.py
#*============================ #
from django.contrib import admin
from .models import Payment
from .models import Plan


admin.site.register(Payment)
admin.site.register(Plan)


