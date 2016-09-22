#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	member/admin.py
#*========================== #
from django.contrib import admin
from .models import Member
from .models import ReferralSource


admin.site.register(Member)
admin.site.register(ReferralSource)

