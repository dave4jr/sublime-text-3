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


#	Choices 
# ====================================== #
BOOLEAN_CHOICES = ((0, "No"), (1, "Yes"))



class Class(models.Model):
	name = models.CharField(max_length=150, blank=True, null=True)
	start = models.DateTimeField(verbose_name="Start Time", blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(verbose_name="End Time", blank=True, null=True, default=datetime.datetime.now)

	def duration(self):
		return (self.end - self.start).days
	duration = property(duration)
	
	teacher = models.ForeignKey(Member, null=True, blank=True)
	price = models.IntegerField(blank=True, null=True)
	discount = models.IntegerField(blank=True, null=True, default=0)
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
	is_private = models.CharField(max_length=10, blank=True, null=True, choices=BOOLEAN_CHOICES, default=0)
	photo = models.ImageField(upload_to="/classes/", null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)
	modified_date = models.DateTimeField(auto_now=True, null=True)
	created_by = models.OneToOneField(User, null=True)

	class Meta:
        	verbose_name_plural = "Classes"

	def __unicode__(self):
		return self.name





