#*============================ #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	context_processors.py
#*============================ #
from .models import Preference


def preference(request):
	preference = Preference.objects.get(pk=1)
	return { 'preference':preference }

