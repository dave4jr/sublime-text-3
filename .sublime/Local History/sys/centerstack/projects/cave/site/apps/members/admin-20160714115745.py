#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	member/admin.py
#*========================== #
from django.contrib import admin
from .models import Member
from .models import ReferralSource
from .models import Expertise
from import_export.admin import ImportExportModelAdmin


class MemberAdmin(ImportExportModelAdmin):
	pass

admin.site.register(Member)
admin.site.register(ReferralSource)
admin.site.register(Expertise)

