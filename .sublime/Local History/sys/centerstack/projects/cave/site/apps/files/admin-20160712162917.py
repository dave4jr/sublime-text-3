#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	files/admin.py
#*============================ #
from django.contrib import admin
from .models import Document

admin.site.register(Document)
