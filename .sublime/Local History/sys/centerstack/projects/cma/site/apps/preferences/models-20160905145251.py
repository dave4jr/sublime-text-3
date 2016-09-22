#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	preferences/models.py
#*======================== #
from django.db import models
from colorfield.fields import ColorField
from django.utils import dateformat
from django.conf import settings
import datetime


class Preference(models.Model):
	global_color = ColorField(default='#fff', null=True)
	calendar_color_tour = ColorField(default='#8d8d8d', null=True)
	calendar_color_class = ColorField(default='#8d8d8d', null=True)
	calendar_color_bike = ColorField(default='#8d8d8d', null=True)
	calendar_color_event = ColorField(default='#8d8d8d', null=True)
	datepicker_color = ColorField(default='#8d8d8d', null=True)

	bike_deposit_multiple = models.IntegerField(verbose_name="Bike Deposit - Daily Rate", blank=True, null=True)
	insurance_high_deductible_price = models.IntegerField(blank=True, null=True)
	insurance_low_deductible_price = models.IntegerField(blank=True, null=True)
	tour_deposit = models.IntegerField(blank=True, null=True)
	tour_deposit_due_lead_time = models.IntegerField(verbose_name="Tour Deposit Due Lead Time (Days)", blank=True, null=True)
	bike_damage_deposit = models.IntegerField(blank=True, null=True)
	storage_price = models.IntegerField(blank=True, null=True)
	custom_onroad = models.IntegerField(blank=True, null=True)
	custom_offroad = models.IntegerField(blank=True, null=True)
	custom_deluxe = models.IntegerField(blank=True, null=True)

	checkin_grace_period = models.DecimalField(verbose_name="Check-In Grace Period (Hours)", max_digits=5, decimal_places=2, null=True, blank=True, default=2)
	
	class Meta:
        	verbose_name_plural = "Preference"

	def __unicode__(self):
		return "Preference #%s" % self.id
