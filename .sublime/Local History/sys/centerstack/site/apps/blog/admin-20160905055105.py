#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	blog/admin.py
#*========================== #
from django.contrib import admin
from .models import Blog
from .models import Group


class GroupAdmin(admin.ModelAdmin):
	list_display 			= ("id", "name",)
	list_display_links 		= ("name",)
	ordering 			= ("id",)
admin.site.register(Group, GroupAdmin)



class BlogAdmin(admin.ModelAdmin):
	list_display 			= ("id", "title", "author", "group", "date", "time")
	list_display_links 		= ("title",)
	ordering 			= ("datetime",)
	save_as 			= True
admin.site.register(Blog, BlogAdmin)


