#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	profiles/models.py
#*======================== #
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime, logging


class OfficeLocation(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return self.name




class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True)
	location = models.ForeignKey(OfficeLocation, null=True, blank=True)

	def __unicode__(self):
		return str(self.user)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

# def view_foo(request):
#     url = request.user.profile.url


