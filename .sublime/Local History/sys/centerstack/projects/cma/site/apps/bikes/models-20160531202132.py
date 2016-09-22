#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	bikes/models.py
#*======================== #
from django.db import models
from django.db.models import Max
import datetime
import logging

START_YEAR = 2010
YEAR_CHOICES = [(r,r) for r in range(START_YEAR, datetime.date.today().year+2)]
PRICE_PERIOD_CHOICES = (("One-Time", "One-Time"), ("Daily", "Daily"), ("Hourly", "Hourly"))
PURCHASE_CONDITION_CHOICES = (("New", "New"), ("Used", "Used"))


class Color(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name = "Color"
	def __unicode__(self):
		return self.name


class Manufacturer(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	class Meta:
		verbose_name = "Manufacturer"
	def __unicode__(self):
		return self.name


class BikeAccessories(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	price = models.IntegerField(blank=True, null=True)
	price_period = models.CharField(max_length=100, blank=True, null=True, choices=PRICE_PERIOD_CHOICES, default="Per Day")
	class Meta:
		verbose_name_plural = "Bike Accessories"
	def __unicode__(self):
		return self.name



class Bike(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Motorcycle")
	manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)
	model = models.CharField(max_length=50, blank=True, null=True)
	color = models.ForeignKey(Color, null=True, blank=True)
	year = models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True, default=datetime.datetime.now().year)
	displacement = models.CharField(max_length=10, blank=True, null=True)
	current_milage = models.IntegerField(blank=True, null=True, default=0)
	rental_price = models.IntegerField(verbose_name="Rental Price", blank=True, null=True)


	#	Image / Color
	# ====================================== #
	image = models.FileField(upload_to='Bikes', blank=True, null=True)

	def status(self):
		reservation = self.reservation_set.all()
		if reservation:
			return "Rented"
		else:
			return "Available"
	status = property(status)


	#	Maintenance Work
	# ====================================== #
	oil_change_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	oil_change_milage = models.IntegerField(blank=True, null=True, default=current_milage)
	air_filter_clean_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	air_filter_clean_milage = models.IntegerField(blank=True, null=True, default=current_milage)
	sprocket_and_chain_change_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	sprocket_and_chain_change_milage = models.IntegerField(blank=True, null=True, default=current_milage)
	valve_adjustment_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	valve_adjustment_milage = models.IntegerField(blank=True, null=True, default=current_milage)
	brake_fluid_change_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	brake_fluid_change_milage = models.IntegerField(blank=True, null=True, default=current_milage)
	coolant_change_date = models.DateField(blank=True, null=True, default=datetime.date.today)
	coolant_change_milage = models.IntegerField(blank=True, null=True, default=current_milage)


	#	Maintenance Schedule
	# ====================================== #
	milage_per_oil_change = models.IntegerField(blank=True, null=True, default=4000)
	milage_per_air_filter_clean = models.IntegerField(blank=True, null=True, default=6000)
	milage_per_sprocket_and_chain_change = models.IntegerField(blank=True, null=True, default=20000)
	milage_per_valve_adjustment = models.IntegerField(blank=True, null=True, default=15000)
	milage_per_brake_fluid_change = models.IntegerField(blank=True, null=True, default=15000)
	milage_per_coolant_change = models.IntegerField(blank=True, null=True, default=20000)

	notes = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name








