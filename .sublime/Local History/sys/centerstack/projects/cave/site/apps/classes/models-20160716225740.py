#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	classes/models.py
#*======================== #
from django.db import models
import datetime
import logging



class Class(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	start = models.DateTimeField(verbose_name="Start Time", blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(verbose_name="End Time", blank=True, null=True, default=datetime.datetime.now)
	
	def duration(self):
		days = abs((self.end - self.start).days)
		if days < 1:
			return abs((self.end - self.start).hours)
		else:
			return abs((self.end - self.start).days)
	duration = property(duration)
	
	description = models.CharField(max_length=500, blank=True, null=True)
	
	price = models.IntegerField(blank=True, null=True)

	class Meta:
        	verbose_name_plural = "Classes"

	def __unicode__(self):
		return self.name





