#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 feed.py
#*====================== #
import os, sys, django
sys.path.append('/sys/centerstack/projects/bs/site')
sys.path.append('/sys/centerstack/projects/bs/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
from rets.models import Property


properties = Property.objects.all()
for ii in properties:
	ii.keysearch = str(ii.listingrid) + str(ii.listingprice) + str(ii.city) + str(ii.county) + str(ii.listingagentfullname) + str(ii.listingagentnumber) + str(ii.listingdate) + str(ii.marketingremarks) + str(ii.mlnumber) + str(ii.propertytype) + str(ii.region) + str(ii.resicomm) + str(ii.resiexte) + str(ii.resihoa) + str(ii.resihoad) + str(ii.resihoap) + str(ii.resihtco) + str(ii.resiinc1) + str(ii.resiinc2) + str(ii.resiinc3) + str(ii.resiinte) + str(ii.resikitc) + str(ii.resilevl) + str(ii.resipark) + str(ii.resiroom) + str(ii.resistyl) + str(ii.resiview) + str(ii.resiwtrd) + str(ii.state) + str(ii.status) + str(ii.statusdate) + str(ii.streetname) + str(ii.streetnumber) + str(ii.streetsuffix) + str(ii.style) + str(ii.unit) + str(ii.yearbuilt) + str(ii.zipcode)
	ii.save()
	










