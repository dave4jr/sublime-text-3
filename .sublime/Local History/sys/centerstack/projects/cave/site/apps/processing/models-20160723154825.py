#*=========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	members/models.py
#*=========================== #
from django.db import models
from tinymce.models import HTMLField
import datetime


class Processing(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	price = models.FloatField(null=True, blank=True)
	hours = models.IntegerField(null=True, blank=True)
	class Meta:
		verbose_name = "Plan"
	def __unicode__(self):
		return self.name


class Member(models.Model):
	first_name = models.CharField(max_length=40, blank=True, null=True)
	last_name = models.CharField(max_length=40, blank=True, null=True)
	member_id = models.CharField(max_length=10, blank=True, null=True)
	current_plan = models.ForeignKey(Plan, null=True, blank=True)
	hours_remaining = models.FloatField(null=True, blank=True)
	
	
	standing = models.CharField(max_length=10, blank=True, null=True, choices=STATUS_CHOICES, default="Active")
	level = models.ForeignKey(Level, null=True, blank=True)
	dob = models.DateField(blank=True, null=True)
	street = models.CharField(max_length=100, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=20, null=True, choices=STATE_CHOICES, default="Oregon")
	zipcode = models.CharField(max_length=5, blank=True, null=True)
	phone = models.CharField(max_length=14,null=True, blank=True)
	email = models.EmailField(max_length=254, blank=True, null=True)
	emergency_contact_name = models.CharField(verbose_name="Emergency Contact", max_length=40, blank=True, null=True)
	emergency_contact_number = models.CharField(max_length=14,null=True, blank=True)
	emergency_contact_relation = models.CharField(max_length=100,null=True, blank=True)
	referral_source = models.ForeignKey(ReferralSource, null=True, blank=True)
	expertise = models.ManyToManyField(Expertise, blank=True)
	membership_start_date = models.DateField(blank=True, null=True, default=datetime.datetime.today)
	photo = models.ImageField(upload_to='members/', blank=True, null=True)
	certifications = models.ManyToManyField(Certification, blank=True)
	notes = models.TextField(null=True, blank=True)
	
	def get_certifications(self):
		return ", ".join([str(ii.name) for ii in self.certifications.all()])
	get_certifications.short_description = "Certifications"

	def get_expertise(self):
		return ", ".join([str(ii.name) for ii in self.expertise.all()])
	get_expertise.short_description = "Expertise"

	def address(self):
		return "%s %s, %s %s" % (self.street, self.city, self.state, self.zipcode )
	address = property(address)

	def name_first_last(self):
		return "%s %s" % (self.first_name, self.last_name)
	name_first_last = property(name_first_last)

	def name_last_first(self):
		return "%s, %s" % (self.last_name, self.first_name)
	name_last_first = property(name_last_first)
	
	def __unicode__(self):
		return self.name_last_first
