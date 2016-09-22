#*=======================
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack
#*  Description:	 customtags.py
#*=======================
from django import template
from django.core import urlresolvers
register = template.Library()



#	Replace underscore with space
# ====================================== #
@register.filter(name='underscore2space')
def underscore2space(value):
	return value.replace("_", " ")



#	Replace 0 with dashes
# ====================================== #
@register.filter(name='to_dash')
def to_dash(value, arg):
	return value.replace(arg, "---")



#	Active / Open CSS Class
# ====================================== #
@register.simple_tag(takes_context=True)
def active(context, url_name, return_value=' active open', **kwargs):
	matches = current_url_equals(context, url_name, **kwargs)
	return return_value if matches else ''


def current_url_equals(context, url_name, **kwargs):
	resolved = False
	try:
		resolved = urlresolvers.resolve(context.get('request').path)
	except:
		pass
	matches = resolved and resolved.url_name == url_name
	if matches and kwargs:
		for key in kwargs:
			kwarg = kwargs.get(key)
			resolved_kwarg = resolved.kwargs.get(key)
			if not resolved_kwarg or kwarg != resolved_kwarg:
				return False
	return matches