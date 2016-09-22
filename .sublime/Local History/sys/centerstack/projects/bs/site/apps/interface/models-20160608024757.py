#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface.py
#*========================== #
from __future__ import unicode_literals
from django.db import models
import json


BED_CHOICES = (("Any", "Any"), ("1+", "1+"), ("2+", "2+"), ("3+", "3+"), ("4+", "4+"), ("5+", "5+"))
BATH_CHOICES = (("Any", "Any"), ("1+", "1+"), ("1.5+", "1.5+"), ("1.75+", "1.75+"), ("2+", "2+"), ("3+", "3+"), ("4+", "4+"), ("5+", "5+"))
SQ_FT_CHOICES = (("< 600", "< 600"), ("800", "800"), ("1,000", "1,000"), ("1,200", "1,200"), ("1,400", "1,400"), ("1,600", "1,600"), ("1,800", "1,800"), ("2,000", "2,000"), ("2,250", "2,250"), ("2,500", "2,500"), ("2,750", "2,750"), ("3,000", "3,000"), ("3,500", "3,500"), ("4,000", "4,000"), ("5,000", "5,000"), ("6,000", "6,000"), ("7,000", "7,000"), ("8,000", "8,000"), ("9,000", "9,000"), ("10,000", "10,000"), ("> 10,000", "> 10,000"))


class Sell(models.Model):
	address = models.CharField(max_length=100, null=True, blank=True)
	zip_code = models.CharField(max_length=5, null=True, blank=True)
	beds = models.CharField(max_length=10, null=True, blank=True, choices=BED_CHOICES, default="Any")
	baths = models.CharField(max_length=10, null=True, blank=True, choices=BATH_CHOICES, default="Any")
	sq_ft = models.CharField(max_length=10, null=True, blank=True, choices=SQ_FT_CHOICES, default="1,000")
	first_name = models.CharField(max_length=50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)

	def __unicode__(self):
		return self.address


class Contact(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	message = models.TextField()

	def __unicode__(self):
		return self.name








