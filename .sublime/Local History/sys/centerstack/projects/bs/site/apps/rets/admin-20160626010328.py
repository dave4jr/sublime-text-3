#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/admin.py
#*========================== #
from django.contrib import admin
from .models import RetsData
from .models import Property

class RetsDataAdmin(admin.ModelAdmin):
	list_display 			= ("id", "update", "json")
	ordering 			= ("update",)
admin.site.register(RetsData, RetsDataAdmin)
admin.site.register(Property)


