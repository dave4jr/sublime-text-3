#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	classes/admin.py
#*============================ #
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Class



class ClassAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Class._meta.fields]
admin.site.register(Class, ClassAdmin)
	






