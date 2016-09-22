#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 migration/views.py
#*====================== #



#	Main
# ====================================== #
def main(request, template):
	context = {}
	return render(request, template, context)


