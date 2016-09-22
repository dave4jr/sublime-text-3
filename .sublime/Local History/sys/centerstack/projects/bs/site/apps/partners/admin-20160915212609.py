#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/admin.py
#*========================== #
from django.contrib import admin
from .models import Partner
from .models import Group


class PartnerAdmin(admin.ModelAdmin):
	list_display  		= [f.name for f in Partner._meta.fields]
	list_display_links 	= ("name",)
	ordering 			= ("name",)
	save_as 			= True
admin.site.register(Partner, PartnerAdmin)



class GroupAdmin(admin.ModelAdmin):
	list_display  		= [f.name for f in Group._meta.fields]
	list_display_links 	= ("name",)
	ordering 			= ("name",)
	save_as 			= True
admin.site.register(Group, GroupAdmin)


