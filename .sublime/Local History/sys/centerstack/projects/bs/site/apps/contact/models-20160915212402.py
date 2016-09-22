#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/models.py
#*=========================== #
from django.db import models
import datetime


class Contact(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField(null=True, blank=True)
	message = models.TextField(blank=True, null=True)
	contact_date = models.DateField(auto_now_add=True, null=True)

	class Meta:
	       verbose_name_plural = "Contact"

	def __unicode__(self):
		return self.email









