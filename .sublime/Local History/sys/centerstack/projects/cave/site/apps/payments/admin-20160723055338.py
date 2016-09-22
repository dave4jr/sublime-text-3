#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/admin.py
#*============================ #
from django.contrib import admin
from .models import Payment


admin.site.register(Payment)


