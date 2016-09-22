# -*- coding: utf-8 -*-
#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	reservations/models.py
#*=========================== #
from django.db import models
from django.utils import dateformat
from customers.models import Customer
from preferences.models import Preference
from classes.models import Class
from tours.models import Tour
from tours.models import TourAccessories
from bikes.models import Bike
from bikes.models import BikeAccessories
from .functions import monthdiff
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_xworkflows import models as wf
from simple_history.models import HistoricalRecords
import logging
import datetime


#	Choices & Functions
# ========================= #
preference, created = Preference.objects.update_or_create(pk=1)
YES_NO_CHOICES = (("Yes", "Yes"), ("No", "No"))
TYPE_CHOICES = (("bike", "Bike"), ("tour", "Tour"), ("tour_bike", "Tour / Bike"), ("class", "Class"), ("class_bike", "Class / Bike"), ("storage", "Storage"))
PRICE_PERIOD_CHOICES = (("One-Time", "One-Time"), ("Daily", "Daily"), ("Hourly", "Hourly"), ("Monthly", "Monthly"), ("Bi-Annual", "Bi-Annual"), ("Annual", "Annual"))
FLEX_CHOICES = ((5, u'±5 Days'), (4, u'±4 Days'), (3, u'±3 Days'), (2, u'±2 Days'), (1, u'±1 Day'), ("Exact", "Exact"))
STORAGE_BIKE_NUM_CHOICES = (("1 Bike", "1 Bike"),("2 Bikes", "2 Bikes"),("3 Bikes", "3 Bikes"),("4 Bikes", "4 Bikes"),("5 Bikes", "5 Bikes"))
TOUR_ROOM_TYPE_CHOICES = (("Single", "Single"),("Shared", "Shared"))


# ==================================================#
#	Workflows
# ==================================================#
class Workflow(wf.Workflow):
	states = (
		('pending_deposit', 'Pending Deposit'),
		('reserved', 'Reserved'),
		('checked_out', 'Checked Out'),
		('checked_in', 'Checked In'),
		('pending_damage_payment', 'Pending Damage Payment'),
	)
	transitions = (
		('receive_deposit', 'pending_deposit', 'reserved'),
		('checkout', 'reserved', 'checked_out'),
		('checkin_no_damage', 'checked_out', 'checked_in'),
		('checkin_yes_damage', 'checked_out', 'pending_damage_payment'),
		('receive_damage_payment', 'pending_damage_payment', 'checked_in'),
		('reset', ("pending_deposit", "reserved", "checked_out", "checked_in", "pending_damage_payment"), 'pending_deposit'),
	)
	initial_state = 'pending_deposit'



# ==================================================#
#	Storage Accessories
# ==================================================#
class StorageAccessories(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	price = models.IntegerField(blank=True, null=True)
	price_period = models.CharField(max_length=100, blank=True, null=True, choices=PRICE_PERIOD_CHOICES, default="One-Time")
	class Meta:
		verbose_name_plural = "Storage Accessories"
	def __unicode__(self):
		return self.name


# ==================================================#
#	Reservation Group
# ==================================================#
class Group(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	def __unicode__(self):
		return self.name


# ==================================================#
#	Reservation
# ==================================================#
class Reservation(wf.WorkflowEnabled, models.Model):
	customer = models.ForeignKey(Customer, null=True, blank=True)
	group = models.ForeignKey(Group, null=True, blank=True)
	rental_type = models.CharField(max_length=20, null=True, blank=True, choices=TYPE_CHOICES)
	status = wf.StateField(Workflow, null=True)
	tour = models.ForeignKey(Tour, null=True, blank=True)
	tour_accessories = models.ManyToManyField(TourAccessories, blank=True)
	
	def get_tour_accessories(self):
		return ", ".join([str(ii.name) for ii in self.tour_accessories.all()])
	get_tour_accessories.short_description = "Tour Accessories"

	tour_room_type = models.CharField(max_length=10, blank=True, null=True, choices=TOUR_ROOM_TYPE_CHOICES, default="Shared")
	classes = models.ForeignKey(Class, null=True, blank=True)
	storage_bike = models.CharField(max_length=50, null=True, blank=True)

	storage_accessories = models.ManyToManyField(StorageAccessories, blank=True)
	def get_storage_accessories(self):
		return ", ".join([str(ii.name) for ii in self.storage_accessories.all()])
	get_storage_accessories.short_description = "Storage Accessories"

	def get_event(self):
		if self.classes is None:
			return "---"
		if self.rental_type == "class" or self.rental_type == "class_bike":
			return self.classes.name
		elif self.rental_type == "tour" or self.rental_type == "tour_bike":
			return self.tour.name
		else:
			return "---"
	event = property(get_event)
	bike = models.ForeignKey(Bike, null=True, blank=True)
	bike_accessories = models.ManyToManyField(BikeAccessories, blank=True)
	def get_bike_accessories(self):
		return ", ".join([str(ii.name) for ii in self.bike_accessories.all()])
	get_bike_accessories.short_description = "Bike Accessories"

	def get_bike_accessories_price(self):
		bike_accessories_sum = []
		for ii in self.bike_accessories.all():
			if ii.price_period == "One-Time":
				bike_accessories_sum.append(ii.price)
			elif ii.price_period == "Daily":
				bike_accessories_sum.append(ii.price * self.duration)
			else:
				pass
		return sum(bike_accessories_sum)


	def bike_final(self):
		if self.rental_type == "tour_bike" and (self.bike is None or self.bike == "" or self.bike == 0):
			return "Personal Bike"
		elif self.rental_type == "class_bike" and (self.bike is None or self.bike == "" or self.bike == 0):
			return "Personal Bike"
		elif self.rental_type == "bike" or self.rental_type == "tour_bike" or self.rental_type == "class_bike":
			return self.bike
		elif self.rental_type == "storage":
			return self.storage_bike
		else:
			return "---"
	bike_final = property(bike_final)

	def get_accessories_final(self):
		accessories = ", ".join([str(ii.name) for ii in self.bike_accessories.all()] + [str(ii.name) for ii in self.storage_accessories.all()] +[str(ii.name) for ii in self.tour_accessories.all()])
		if (accessories is None or accessories == "" or accessories == 0):
			return "---"
		else:
			return accessories

	checkout_datetime = models.DateTimeField(verbose_name="Check-Out", blank=True, null=True, default=datetime.datetime.now)
	checkin_datetime = models.DateTimeField(verbose_name="Check-In", blank=True, null=True, default=datetime.datetime.now)

	def duration(self):
		return abs((self.checkin_datetime - self.checkout_datetime).days)
	duration = property(duration)
	start = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
	flexibility = models.CharField(max_length=20, null=True, blank=True, choices=FLEX_CHOICES, default="Exact")

	def available(self):
		if (self.start < self.checkout_datetime) and (self.end < self.checkin_datetime):
			return "Available:"
		elif (self.start < self.checkout_datetime):
			return "Check-Out Available:"
		elif (self.end < self.checkin_datetime):
			return "Check-In Available:"
		else:
			return "Unavailable"
	available = property(available)




# ==================================================#
#	Checkout
# ==================================================#
	checkout_datetime_actual = models.DateTimeField(verbose_name="Check-Out (Actual)", blank=True, null=True, default=datetime.datetime.now)
	checkout_milage = models.IntegerField(blank=True, null=True)
	checkout_img_1 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_img_2 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_img_3 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_img_4 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_img_5 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_img_6 = models.FileField(upload_to='Check-Out/%Y/%m/', blank=True, null=True)
	checkout_notes = models.TextField(blank=True, null=True)

	def get_name(self):
		fn = str(self.file).lower()
		return os.path.basename(fn)
	name = property(get_name)

	def size_mb(self):
		return self.file.size / 1000
	size_mb = property(size_mb)

	checkout_file_created = models.DateTimeField(auto_now_add=True, null=True)
	checkout_file_modified = models.DateTimeField(auto_now=True, null=True)



# ==================================================#
#	Checkin
# ==================================================#
	checkin_datetime_actual = models.DateTimeField(verbose_name="Check-In (Actual)", blank=True, null=True, default=datetime.datetime.now)

	def is_late(self):
		if self.checkin_datetime_actual > (self.checkin_datetime + preference.checkin_grace_period):
			return (self.checkin_datetime_actual - self.checkin_datetime).hours
		else:
			return False


	checkin_milage = models.IntegerField(blank=True, null=True)

	def trip_milage(self):
		return self.checkin_milage - self.checkout_milage
	trip_milage = property(trip_milage)


	is_damaged = models.BooleanField(default=0, blank=True)
	checkin_img_1 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_img_2 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_img_3 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_img_4 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_img_5 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_img_6 = models.FileField(upload_to='Check-In/%Y/%m/', blank=True, null=True)
	checkin_notes = models.TextField(blank=True, null=True)



# ==================================================#
#	Pricing
# ==================================================#
	def bike_deposit(self):
		if self.bike is None:
			return 0
		elif self.rental_type in ["bike", "tour_bike", "class_bike"]:
			return (preference.bike_deposit_multiple * self.duration)
		else:
			return 0
	bike_deposit = property(bike_deposit)


	#	Bike Damage Deposit
	# ====================================== #
	def bike_damage_deposit(self):
		if "bike" in self.rental_type:
			return preference.bike_damage_deposit
		else:
			return 0
	bike_damage_deposit = property(bike_damage_deposit)


	#	Tour Deposit
	# ====================================== #
	def tour_deposit(self):
		if "tour" in self.rental_type:
			return preference.tour_deposit
		else:
			return 0
	tour_deposit = property(tour_deposit)


	#	Bike Insurance
	# ====================================== #
	def bike_insurance(self):
		if self.bike is None:
			return 0
		else:
			return (preference.insurance_price * self.duration)
	bike_insurance = property(bike_insurance)

	
	#	Bike Price
	# ====================================== #
	def bike_price(self):
		if self.bike is None:
			return 0
		else:
			return (self.bike.rental_price * self.duration)
	bike_price = property(bike_price)


	#	Tour Price
	# ====================================== #
	def tour_price(self):
		if self.tour is None:
			return 0
		elif self.tour_room_type == "Shared":
			return self.tour.price_shared
		elif self.tour_room_type == "Single":
			return self.tour.price_single
		else:
			return 0
	tour_price = property(tour_price)


	#	Class Price
	# ====================================== #
	def class_price(self):
		if self.classes is None:
			return 0
		else:
			return self.classes.price
	class_price = property(class_price)


	#	Storage Price
	# ====================================== #
	def storage_price(self):
		if self.rental_type == "storage":
			months = monthdiff(preference.storage_price * months)
		else:
			return 0
	storage_price = property(storage_price)


	#	Total Deposit
	# ====================================== #
	def total_deposit(self):
		return self.bike_deposit + self.tour_deposit
	total_deposit = property(total_deposit)


	#	Total Price
	# ====================================== #
	def total_price(self):
		return self.bike_insurance + self.bike_price + self.tour_price + self.class_price + self.storage_price
	total_price = property(total_price)


	#	Final Price (Deducted Deposit)
	# ====================================== #
	def final_price(self):
		return self.total_price - self.total_deposit
	final_price = property(final_price)

	discount = models.IntegerField(verbose_name="Group Discount (%)", blank=True, null=True)
	tax_rate = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Tax Rate (%)", blank=True, null=True, default=10.00)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	modified = models.DateTimeField(auto_now=True, null=True, blank=True)
	history = HistoricalRecords()

	def __unicode__(self):
		return str(self.customer)





# ==================================================#
#	Search
# ==================================================#
class Search(models.Model):
	reservation = models.ForeignKey(Reservation, null=True, blank=True)
	bike = models.ForeignKey(Bike, null=True, blank=True)
	start = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
	end = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
	flexibility = models.CharField(max_length=20, null=True, blank=True, choices=FLEX_CHOICES, default="Exact")

	def available(self):
		if (self.start < self.reservation.checkout_datetime) and (self.end < self.reservation.checkin_datetime):
			return "Available: %s" % self.reservation.bike
		elif (self.start < self.reservation.checkout_datetime):
			return "Check-Out Available: %s" % self.reservation.bike
		elif (self.end < self.reservation.checkin_datetime):
			return "Check-In Available: %s" % self.reservation.bike
		else:
			return "Unavailable"
	available = property(available)

	def __unicode__(self):
		return self.bike






# send_confirmation_email = models.BooleanField(verbose_name="Send Confirmation Email", default=False)



#	Confirmation Emails
# ================================ #
# @receiver(post_save, sender=Reservation)
# def send_confirmation_email(sender, **kwargs):
# 	reservation = kwargs['instance']
# 	bike = Bike.objects.get(pk=reservation.pk)
# 	customer = Customer.objects.get(pk=reservation.pk)
# 	if reservation.send_confirmation_email:
# 		html_content = render_to_string('email/confirmation.html', {'reservation': reservation, 'bike':bike, 'customer':customer})
# 		text_content = "CMA Reservation Confirmation"
# 		subject = "CMA Reservation Confirmation"
# 		from_email = "info@coloradomotorcycleadventures.com"
# 		to_email = customer.email
# 		send_mail(subject, text_content, from_email, [to_email], html_message=html_content)
# 		reservation.send_confirmation_email = False
# 		reservation.save()








