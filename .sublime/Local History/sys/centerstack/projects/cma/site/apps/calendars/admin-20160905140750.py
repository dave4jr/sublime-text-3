#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	calendar/admin.py
#*============================ #
from django.contrib import admin
from .models import Calendar


class CalendarAdmin(admin.ModelAdmin):
	list_display  = [f.name for f in Calendar._meta.fields]
admin.site.register(Calendar, CalendarAdmin)




