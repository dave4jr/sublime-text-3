#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	calendars/models.py
#*======================== #
from django.db import models
import datetime
import logging


class Calendar(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	start = models.DateTimeField(verbose_name="Start Time", blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(verbose_name="End Time", blank=True, null=True, default=datetime.datetime.now)
	notes = models.TextField(null=True, blank=True)
	
	def duration(self):
		days = abs((self.end - self.start).days)
		if days < 1:
			return abs((self.end - self.start).hours)
		else:
			return abs((self.end - self.start).days)
	duration = property(duration)

	class Meta:
        	verbose_name_plural = "Calendar"

	def __unicode__(self):
		return self.name





