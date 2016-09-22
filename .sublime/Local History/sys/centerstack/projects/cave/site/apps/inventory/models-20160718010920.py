#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/models.py
#*======================== #
from django.db import models
from django.contrib.auth.models import User
from members.models import Member
import datetime
import logging


#	Choices 
# ====================================== #
BOOLEAN_CHOICES = ((0, "No"), (1, "Yes"))



class Inventory(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to="/inventory/", null=True, blank=True)

	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modified_date = models.DateTimeField(auto_now=True, null=True)
	created_by = models.OneToOneField(User, null=True)

	class Meta:
        	verbose_name_plural = "Inventory"

	def __unicode__(self):
		return self.name





