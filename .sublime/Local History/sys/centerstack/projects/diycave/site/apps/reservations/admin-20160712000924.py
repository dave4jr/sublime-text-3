#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	reservations/admin.py
#*============================ #
from django.contrib import admin
from .models import Reservation
from .models import Group


admin.site.register(Reservation)
admin.site.register(Group)





