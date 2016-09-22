#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 migration/views.py
#*====================== #
from django.shortcuts import render


#	Main
# ====================================== #
def main(request, template):
	context = {}
	return render(request, template, context)


