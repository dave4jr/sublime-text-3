#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	member/admin.py
#*========================== #
from django.contrib import admin
from .models import Member
from .models import Level
from .models import ReferralSource
from .models import Expertise
from import_export.admin import ImportExportModelAdmin


class MemberAdmin(ImportExportModelAdmin):
	list_display  = [f.name for f in Member._meta.fields]


admin.site.register(Member, MemberAdmin)
admin.site.register(ReferralSource)
admin.site.register(Level)
admin.site.register(Expertise)

