#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/models.py
#*======================== #
from django.db import models
from django.contrib.auth.models import User
from members.models import Member
from annoying.fields import JSONField
import datetime
import logging

#	Choices 
# ====================================== #
BOOLEAN_CHOICES = ((0, "No"), (1, "Yes"))



class Group(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self):
		return self.item


class Inventory(models.Model):
	title = models.CharField(max_length=150, blank=True, null=True)
	upc = models.CharField(max_length=12, blank=True, null=True)
	group = models.ForeignKey(Group, null=True, blank=True)
	description = models.TextField(blank=True, null=True)
	brand = models.CharField(max_length=50, blank=True, null=True)
	images = JSONField(null=True, blank=True)
	pack = models.IntegerField(null=True, blank=True)
	avg_price = models.FloatField(null=True, blank=True)
	quantity = models.IntegerField(null=True, blank=True)
	cost = models.FloatField(null=True, blank=True)
	vendor = models.CharField(max_length=12, blank=True, null=True)
	markup = models.IntegerField(null=True, blank=True)
	retail = models.FloatField(null=True, blank=True)
	notes = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modified_date = models.DateTimeField(auto_now=True, null=True)

	class Meta:
        	verbose_name_plural = "Inventory"

	def __unicode__(self):
		return self.item





