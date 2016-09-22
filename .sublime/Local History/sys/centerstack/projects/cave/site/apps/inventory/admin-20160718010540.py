#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Inventoryes/admin.py
#*============================ #
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Inventory



class InventoryAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Inventory._meta.fields]
admin.site.register(Inventory, InventoryAdmin)
	






