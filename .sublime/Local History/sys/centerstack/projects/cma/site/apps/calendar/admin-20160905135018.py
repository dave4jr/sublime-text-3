#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	classes/admin.py
#*============================ #
from django.contrib import admin
from .models import Calendar

@admin.register(Calendar)
CalendarAdmin(admin.ModelAdmin):
	list_display  = [f.name for f in Calendar._meta.fields]





