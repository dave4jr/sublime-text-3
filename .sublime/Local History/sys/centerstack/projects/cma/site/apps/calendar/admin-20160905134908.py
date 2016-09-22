#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	classes/admin.py
#*============================ #
from django.contrib import admin
from .models import Calendar

@admin.register(Calendar)
Calendar ClassAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "teacher", "price")
	list_display_links = ("name",)
	ordering = ('id',)




