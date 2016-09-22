#*=======================
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack
#*  Description:	 html_functions.py
#*=======================
from django import template
from django.http import HttpResponse

register = template.Library()

# @register.simple_tag(takes_context=True)
# def heading(request, heading_name):
# 	html = "<div class="heading"><h3 class="heading-tag">%s</h3><div class="heading-border"><div class="heading-border-inner-border"></div></div></div>" % heading_name
# 	return render(html)



