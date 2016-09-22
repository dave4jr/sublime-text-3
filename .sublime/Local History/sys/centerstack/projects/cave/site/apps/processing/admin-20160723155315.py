#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	processing/admin.py
#*========================== #
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProcessingAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Processing._meta.fields]


admin.site.register(Processing, ProcessingAdmin)

