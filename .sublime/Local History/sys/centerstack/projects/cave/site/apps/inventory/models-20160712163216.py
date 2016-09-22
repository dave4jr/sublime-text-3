#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/models.py
#*======================== #
from django.db import models
from django.db.models import Max
import datetime
import logging

START_YEAR = 2010
YEAR_CHOICES = [(r,r) for r in range(START_YEAR, datetime.date.today().year+2)]
PRICE_PERIOD_CHOICES = (("One-Time", "One-Time"), ("Daily", "Daily"))
PURCHASE_CONDITION_CHOICES = (("New", "New"), ("Used", "Used"))


class Bike(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Motorcycle")
	model = models.CharField(max_length=50, blank=True, null=True)
	year = models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year)
	displacement = models.CharField(max_length=10, blank=True, null=True)
	license_plate = models.CharField(max_length=15, blank=True, null=True)
	current_mileage = models.IntegerField(blank=True, null=True)
	rental_price = models.IntegerField(verbose_name="Rental Price", blank=True, null=True)

	def status(self):
		reservation = self.reservation_set.all()
		if reservation:
			return "Rented"
		else:
			return "Available"
	status = property(status)


	notes = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name








