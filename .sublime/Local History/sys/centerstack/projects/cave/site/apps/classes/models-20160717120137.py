#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	classes/models.py
#*======================== #
from django.db import models
from django.contrib.auth.models import User
from members.models import Member
import datetime
import logging



class Class(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	start = models.DateTimeField(verbose_name="Start Time", blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(verbose_name="End Time", blank=True, null=True, default=datetime.datetime.now)

	def duration(self):
		return (self.end - self.start).days
		# if days < 1:
		# 	h_end = (self.end).hour
		# 	h_start = (self.start).hour
		# 	h_end = (self.end).minute
		# 	h_start = (self.start).minute
		# 	h_end = (self.end).second
		# 	h_start = (self.start).second
		# 	h = d.hour + d.minute / 60. + d.second / 3600.
		# 	return h
		# else:
		# 	return days
	duration = property(duration)
	
	teacher = models.ForeignKey(Member, null=True, blank=True)
	price = models.IntegerField(blank=True, null=True)
	bookings = models.IntegerField(blank=True, null=True, default=0)
	seats = models.IntegerField(blank=True, null=True, default=10)

	def status(self):
		if self.bookings == self.seats:
			return "Full"
		elif self.bookings > self.seats:
			return "Over Sold"
		else:
			return "Open"
	status = property(status)

	description = models.TextField(blank=True, null=True)
	is_private = models.BooleanField(default=0)
	photo = models.ImageField(upload_to="/classes/", null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modified_date = models.DateTimeField(auto_now=True, null=True)
	created_by = models.OneToOneField(User, null=True)

	class Meta:
        	verbose_name_plural = "Classes"

	def __unicode__(self):
		return self.name





