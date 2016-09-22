#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/admin.py
#*============================ #
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import POS


class POSAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in POS._meta.fields]


