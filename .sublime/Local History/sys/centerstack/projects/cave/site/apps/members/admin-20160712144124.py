#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	customer/admin.py
#*========================== #
from django.contrib import admin
from .models import Customer
from .models import ReferralSource


admin.site.register(Customer)
admin.site.register(ReferralSource)

