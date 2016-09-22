#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	rets/models.py
#*========================== #
from __future__ import unicode_literals
from django.db import models
from annoying.fields import JSONField
import datetime



class Property(models.Model):
	property_id 		= models.CharField(max_length=6, null=True, blank=True)
	img				= JSONField(null=True, blank=True)
	bedrooms 			= models.FloatField(null=True, blank=True)
	bathrooms 			= models.FloatField(null=True, blank=True)
	latitude 			= models.FloatField(null=True, blank=True)
	longitude 			= models.FloatField(null=True, blank=True)
	acres 			= models.FloatField(null=True, blank=True)
	squarefootage 		= models.IntegerField(null=True, blank=True)
	propertytype 		= models.CharField(max_length=500, null=True, blank=True)
	city 				= models.CharField(max_length=500, null=True, blank=True)
	
	
	#	New Added Fields
	# ====================================== #
	resifire			= models.CharField(max_length=500, null=True, blank=True)	# Fireplace
	resiflor			= models.CharField(max_length=500, null=True, blank=True)	# Floors
	resiirri			= models.CharField(max_length=500, null=True, blank=True)	# Irrigation Rights (Y/N)
	resiirra			= models.CharField(max_length=500, null=True, blank=True)	# Irrigation Acres
	resiirrd			= models.CharField(max_length=500, null=True, blank=True)	# Irrigation District (Source)
	resisewr			= models.CharField(max_length=500, null=True, blank=True)	# Sewer / Septic
	resinewc			= models.CharField(max_length=500, null=True, blank=True)	# New Construction
	resicons			= models.CharField(max_length=500, null=True, blank=True)	# Construction
	dom				= models.CharField(max_length=500, null=True, blank=True)	# Days-on-Market
	resiaddi			= models.CharField(max_length=500, null=True, blank=True)	# Additional Buildings
	resihtco			= models.CharField(max_length=500, null=True, blank=True)	# Heat / Cool
	resitaxs			= models.CharField(max_length=500, null=True, blank=True)	# Taxes
	resiccr			= models.CharField(max_length=500, null=True, blank=True)	# CC&R
	resisrhi			= models.CharField(max_length=500, null=True, blank=True)	# High School
	resijrhi			= models.CharField(max_length=500, null=True, blank=True)	# Jr High School
	resielms			= models.CharField(max_length=500, null=True, blank=True)	# Elementary School



	#	Keyword Fields
	# ====================================== #
	keysearch 			= models.CharField(max_length=5000, null=True, blank=True)
	listingagentfullname 	= models.CharField(max_length=500, null=True, blank=True)
	listingprice 		= models.IntegerField(null=True, blank=True)
	listingrid 			= models.CharField(max_length=500, null=True, blank=True)
	marketingremarks 	= models.CharField(max_length=500, null=True, blank=True)
	mlnumber 			= models.CharField(max_length=500, null=True, blank=True)
	resicomm 			= models.CharField(max_length=500, null=True, blank=True)
	resiexte 			= models.CharField(max_length=500, null=True, blank=True)
	resihoa 			= models.CharField(max_length=500, null=True, blank=True)
	resihoad 			= models.CharField(max_length=500, null=True, blank=True)
	resihoap 			= models.CharField(max_length=500, null=True, blank=True)
	resihtco 			= models.CharField(max_length=500, null=True, blank=True)
	resiinte 			= models.CharField(max_length=500, null=True, blank=True)
	resilevl 			= models.CharField(max_length=500, null=True, blank=True)
	resipark 			= models.CharField(max_length=500, null=True, blank=True)
	resiroom 			= models.CharField(max_length=500, null=True, blank=True)
	resiwtrd 			= models.CharField(max_length=500, null=True, blank=True)
	section 			= models.CharField(max_length=500, null=True, blank=True)
	state 			= models.CharField(max_length=500, null=True, blank=True)
	status 			= models.CharField(max_length=500, null=True, blank=True)
	streetname 		= models.CharField(max_length=500, null=True, blank=True)
	streetnumber 		= models.CharField(max_length=500, null=True, blank=True)
	streetsuffix 		= models.CharField(max_length=500, null=True, blank=True)
	style	 			= models.CharField(max_length=500, null=True, blank=True)
	subtype	 		= models.CharField(max_length=500, null=True, blank=True)
	unit 				= models.CharField(max_length=500, null=True, blank=True)
	view	 			= models.CharField(max_length=500, null=True, blank=True)
	yearbuilt 			= models.CharField(max_length=500, null=True, blank=True)
	zipcode 			= models.CharField(max_length=500, null=True, blank=True)


	def __unicode__(self):
		return self.listingrid









