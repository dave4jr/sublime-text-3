#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	reservations/admin.py
#*============================ #
from django.contrib import admin
from .models import Reservation


admin.site.register(Reservation)





