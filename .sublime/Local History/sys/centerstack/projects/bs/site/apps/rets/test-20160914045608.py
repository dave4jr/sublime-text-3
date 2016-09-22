#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 feed.py
#*====================== #
import os, sys, django, requests, bs4, re, json
from random import randint

x = ["Acres","Bathrooms","Bedrooms","City","DOM","Latitude","ListingAgentFullName","ListingPrice","ListingRid","Longitude","MarketingRemarks","MLNumber","PropertySubtype1","PropertyType","RESIADDI","RESICCR","RESICOMM","RESICONS","RESIELMS","RESIEXTE","RESIFIRE","RESIFLOR","RESIHOA","RESIHOAD","RESIHOAP","RESIHTCO","RESIINTE","RESIIRRA","RESIIRRD","RESIIRRI","RESIJRHI","RESILEVL","RESINEWC","RESIPARK","RESIROOM","RESISEWR","RESISRHI","RESISTYL","RESITAXS","RESIVIEW","RESIWTRD","SquareFootage","State","Status","StreetName","StreetNumber","StreetSuffix","Style","Unit","YearBuilt","ZipCode"]
defaults = {}

for ii in x:
	print ii
	defaults[ii] = randint(0,9)
print defaults

k = ""	
for field in x:
	k = k + str(defaults[field]) 
print k



