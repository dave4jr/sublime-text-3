#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/admin.py
#*============================ #
from django.contrib import admin
from .models import Payment
from .models import Plan
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Payment, SimpleHistoryAdmin)
admin.site.register(Plan, SimpleHistoryAdmin)


