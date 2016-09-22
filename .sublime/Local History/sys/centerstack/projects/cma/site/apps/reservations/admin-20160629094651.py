#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	reservations/admin.py
#*============================ #
from django.contrib import admin
from .models import Reservation
from .models import Group
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Reservation, SimpleHistoryAdmin)
admin.site.register(Group)




