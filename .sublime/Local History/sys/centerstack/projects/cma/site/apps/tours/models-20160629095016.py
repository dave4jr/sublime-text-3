#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	tours/models.py
#*======================== #
from django.db import models
from django import forms
import datetime
from bikes.models import Bike

PLANNING_STATUS_CHOICES = (("Pending", "Pending"), ("In-progress", "In-Progress"), ("Complete", "Complete"))
SKILL_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), )
PRICE_PERIOD_CHOICES = (("One-Time", "One-Time"), ("Daily", "Daily"), ("Hourly", "Hourly"), ("Monthly", "Monthly"), ("Bi-Annual", "Bi-Annual"), ("Annual", "Annual"))


class Guide(models.Model):
	name = models.CharField(max_length=250, blank=True)
	class Meta:
		verbose_name = "Guide"
	def __unicode__(self):
		return self.name


class Location(models.Model):
	name = models.CharField(max_length=30, blank=True)
	class Meta:
		verbose_name = "Location"
	def __unicode__(self):
		return self.name


class TourPlanning(models.Model):
	checkpoint = models.CharField(max_length=60, blank=True)
	status = models.CharField(max_length=20, blank=True, choices=PLANNING_STATUS_CHOICES, default="pending")
	def __unicode__(self):
		return self.checkpoint


class Tour(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	date_start = models.DateField(null=True, blank=True, default=datetime.datetime.today)
	date_end = models.DateField(null=True, blank=True, default=datetime.datetime.today)

	def status(self):
		now = datetime.datetime.today()
		now = now.date()
		if now >= self.date_start and now <= self.date_end:
			return "In-Progress"
		elif now < self.date_start:
			return "Upcoming"
		elif now > self.date_end:
			return "Completed"
	status = property(status)

	def days_between(self):
		return abs((self.date_end - self.date_start).days)
	duration = property(days_between)
		
	location = models.ForeignKey(Location, null=True, blank=True)
	guide = models.ForeignKey(Guide, null=True, blank=True)
	skill = models.IntegerField(blank=True, null=True, choices=SKILL_CHOICES, default=3)
	mileage = models.IntegerField(blank=True, null=True)
	price_shared = models.IntegerField(verbose_name="Price (Shared)", blank=True, null=True)
	price_single = models.IntegerField(verbose_name="Price (Single)", blank=True, null=True)
	deposit = models.IntegerField(verbose_name="Reservation Deposit", blank=True, null=True, default=1000)
	
	def __unicode__(self):
		return self.name



class BikePrice(models.Model):
	tour = models.ForeignKey(Tour, null=True)
	bike = models.ForeignKey(Bike, null=True)
	price = models.IntegerField(blank=True, null=True)
	def __unicode__(self):
		return self.tour.name









