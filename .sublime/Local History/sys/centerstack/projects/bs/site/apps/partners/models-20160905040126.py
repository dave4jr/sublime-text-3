#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	contact/models.py
#*=========================== #
from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime


class Partner(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	img_banner = models.ImageField(upload_to="", blank=True, null=True)
	intro = HTMLField(blank=True, null=True)

	class Meta:
	       verbose_name_plural = "Contact"

	def __unicode__(self):
		return self.email









