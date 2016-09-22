#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	tours/admin.py
#*======================== #
from django.contrib import admin
from .models import Custom
import logging


class CustomAdmin(admin.ModelAdmin):
	list_display = ("name",)

admin.site.register(Custom, CustomAdmin)


