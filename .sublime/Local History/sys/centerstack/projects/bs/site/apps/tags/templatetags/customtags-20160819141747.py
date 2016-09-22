#*=======================
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack
#*  Description:	 customtags.py
#*=======================
from django import template
from django.core import urlresolvers
from django.utils.safestring import mark_safe
import os, sys
import math
from django.conf import settings
register = template.Library()



#	First Letter Uppercase
# ====================================== #
@register.filter(name='boxed_letter')
def boxed_letter(value, color):
	if value is not None:
		first_letter = value[0]
		rest_of_letters = value[1:]
		html = "<span style='padding: 3px 8px; margin-right: 3px; text-transform: uppercase; color: #fff; background: %s; border-radius: 4px; font-size: 18px; font-weight: 600;'>%s</span>%s" %  (color, first_letter, rest_of_letters)
		return mark_safe(html)


#	Number Filter
# ====================================== #
@register.filter(name='strip')
def strip(value):
	if value is not None:
		v = value.strip()
		return v.lower()



#	Number of Digits Filter
# ====================================== #
@register.filter(name='num_digits')
def num_digits(value):
	if value is not None:
		return int(math.log10(value))+1
		

		

#	Replace underscore with space
# ====================================== #
@register.filter(name='underscore2space')
def underscore2space(value):
	if value is not None:
		return value.replace("_", " ")


#	Replace underscore with &
# ====================================== #
@register.filter(name='underscore2amp')
def underscore2amp(value):
	if value is not None:
		return value.replace("_", " & ")


#	Replace 0 with dashes
# ====================================== #
@register.filter(name='to_dash')
def to_dash(value, arg):
	if value is not None:
		return value.replace(arg, "---")


#	Basename
# ====================================== #
@register.filter(name='getbasename')
def getbasename(value, arg):
	if value is not None:
		s = os.path.join(settings.MEDIA_ROOT, arg)
		return value.strip(s)




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



