#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/upload_data.py
#*========================== #
from __future__ import unicode_literals
from django.db import models
from annoying.fields import JSONField
import datetime


#	Choices
# ====================================== #
BED_CHOICES = (("Any", "Any"), ("1+", "1+"), ("2+", "2+"), ("3+", "3+"), ("4+", "4+"), ("5+", "5+"))
BATH_CHOICES = (("Any", "Any"), ("1+", "1+"), ("1.5+", "1.5+"), ("1.75+", "1.75+"), ("2+", "2+"), ("3+", "3+"), ("4+", "4+"), ("5+", "5+"))
SQ_FT_CHOICES = (("< 600", "< 600"), ("800", "800"), ("1,000", "1,000"), ("1,200", "1,200"), ("1,400", "1,400"), ("1,600", "1,600"), ("1,800", "1,800"), ("2,000", "2,000"), ("2,250", "2,250"), ("2,500", "2,500"), ("2,750", "2,750"), ("3,000", "3,000"), ("3,500", "3,500"), ("4,000", "4,000"), ("5,000", "5,000"), ("6,000", "6,000"), ("7,000", "7,000"), ("8,000", "8,000"), ("9,000", "9,000"), ("10,000", "10,000"), ("> 10,000", "> 10,000"))



class Image(models.Model):
	image_id	 		= models.CharField(max_length=100, null=True, blank=True)
	property_id 		= models.CharField(max_length=100, null=True, blank=True)
	img 				= models.CharField(max_length=300, null=True, blank=True)

	def __unicode__(self):
		return self.img


class Property(models.Model):
	property_id 		= models.CharField(max_length=100, null=True, blank=True)
	img				= models.ManyToManyField(Image, blank=True)
	city 				= models.CharField(max_length=100, null=True, blank=True)
	county 			= models.CharField(max_length=100, null=True, blank=True)
	bedrooms 			= models.CharField(max_length=100, null=True, blank=True)
	bathrooms 			= models.CharField(max_length=100, null=True, blank=True)
	squarefootage 		= models.CharField(max_length=100, null=True, blank=True)
	acres 				= models.CharField(max_length=100, null=True, blank=True)
	listingprice 			= models.CharField(max_length=100, null=True, blank=True)
	area 				= models.CharField(max_length=100, null=True, blank=True)
	latitude 			= models.CharField(max_length=100, null=True, blank=True)
	listingagentfullname 	= models.CharField(max_length=100, null=True, blank=True)
	listingagentnumber 	= models.CharField(max_length=100, null=True, blank=True)
	listingdate 			= models.CharField(max_length=100, null=True, blank=True)
	listingrid 			= models.CharField(max_length=100, null=True, blank=True)
	longitude 			= models.CharField(max_length=100, null=True, blank=True)
	lotmeasurement 		= models.CharField(max_length=100, null=True, blank=True)
	lotsquarefootage 		= models.CharField(max_length=100, null=True, blank=True)
	marketingremarks 	= models.CharField(max_length=100, null=True, blank=True)
	mlnumber 			= models.CharField(max_length=100, null=True, blank=True)
	propertytype 		= models.CharField(max_length=100, null=True, blank=True)
	region 			= models.CharField(max_length=100, null=True, blank=True)
	resicomm 			= models.CharField(max_length=100, null=True, blank=True)
	resiexte 			= models.CharField(max_length=100, null=True, blank=True)
	resihoa 			= models.CharField(max_length=100, null=True, blank=True)
	resihoad 			= models.CharField(max_length=100, null=True, blank=True)
	resihoap 			= models.CharField(max_length=100, null=True, blank=True)
	resihtco 			= models.CharField(max_length=100, null=True, blank=True)
	resiinc1 			= models.CharField(max_length=100, null=True, blank=True)
	resiinc2 			= models.CharField(max_length=100, null=True, blank=True)
	resiinc3 			= models.CharField(max_length=100, null=True, blank=True)
	resiinte 			= models.CharField(max_length=100, null=True, blank=True)
	resikitc 			= models.CharField(max_length=100, null=True, blank=True)
	resilevl 			= models.CharField(max_length=100, null=True, blank=True)
	resipark 			= models.CharField(max_length=100, null=True, blank=True)
	resiroom 			= models.CharField(max_length=100, null=True, blank=True)
	resistyl 			= models.CharField(max_length=100, null=True, blank=True)
	resiview 			= models.CharField(max_length=100, null=True, blank=True)
	resiwtrd 			= models.CharField(max_length=100, null=True, blank=True)
	state 				= models.CharField(max_length=100, null=True, blank=True)
	status 			= models.CharField(max_length=100, null=True, blank=True)
	statusdate 			= models.CharField(max_length=100, null=True, blank=True)
	streetname 		= models.CharField(max_length=100, null=True, blank=True)
	streetnumber 		= models.CharField(max_length=100, null=True, blank=True)
	streetsuffix 		= models.CharField(max_length=100, null=True, blank=True)
	style 				= models.CharField(max_length=100, null=True, blank=True)
	unit 				= models.CharField(max_length=100, null=True, blank=True)
	yearbuilt 			= models.CharField(max_length=100, null=True, blank=True)
	zipcode 			= models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return self.listingrid









