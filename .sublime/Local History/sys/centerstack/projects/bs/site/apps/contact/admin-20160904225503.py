#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/admin.py
#*========================== #
from django.contrib import admin
from .models import Contact

class ContactAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Inventory._meta.fields]
admin.site.register(Inventory, InventoryAdmin)
class ContactAdmin(admin.ModelAdmin):
	list_display 			= ("id", "name", "email", "message", "contact_date")
	list_display_links 		= ("name",)
	ordering 			= ("contact_date",)
	save_as 			= True
admin.site.register(Contact, ContactAdmin)


