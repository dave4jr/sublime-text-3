#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	classes/admin.py
#*============================ #
from django.contrib import admin
from .models import Class


class ClassAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "created_by", "modified_by")
	list_display_links = ("name",)
	ordering = ('id',)
admin.site.register(Class, ClassAdmin)







