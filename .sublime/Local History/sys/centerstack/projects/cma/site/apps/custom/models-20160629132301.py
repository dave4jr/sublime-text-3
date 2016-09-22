#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	custom/models.py
#*======================== #
from django.db import models
from django import forms
import datetime
from tinymce.models import HTMLField


#	Choices
# ====================================== #
SKILL_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), )


class Custom(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	location = models.CharField(max_length=200, null=True, blank=True)
	skill = models.IntegerField(blank=True, null=True, choices=SKILL_CHOICES, default=3)
	mileage = models.IntegerField(blank=True, null=True)
	price = models.IntegerField(verbose_name="Price", blank=True, null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	notes = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name



