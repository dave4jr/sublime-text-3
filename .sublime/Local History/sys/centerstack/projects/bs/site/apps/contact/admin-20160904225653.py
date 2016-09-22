#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/admin.py
#*========================== #
from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin


class ContactAdmin(ImportExportModelAdmin):
	list_display  		= [f.name for f in Contact._meta.fields]
	list_display_links 	= ("name",)
	ordering 			= ("contact_date",)
	save_as 			= True
admin.site.register(Contact, ContactAdmin)


