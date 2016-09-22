#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/admin.py
#*========================== #
from django.contrib import admin
from .models import Property
from .models import Image



#	Image
# ====================================== #
class ImageAdmin(admin.ModelAdmin):
	list_display 			= ("id", "property_id", "img")
	ordering 			= ("id",)
admin.site.register(Image, ImageAdmin)


#	Property
# ====================================== #
class PropertyAdmin(admin.ModelAdmin):
	list_display 			= ("id", "acres","area","bathrooms","bedrooms","city","county","img","latitude","listingagentfullname","listingdate","listingprice","listingrid","longitude","mlnumber","propertytype","region","resiexte","resihoa","resihoad","resihoap","resihtco","resiinc1","resiinc2","resiinc3","resiinte","resikitc","resilevl","resipark","resiroom","resistyl","resiview","resiwtrd","squarefootage","state","status","statusdate","streetname","streetnumber","streetsuffix","style","unit","yearbuilt","zipcode")
	ordering 			= ("id",)
admin.site.register(Property, PropertyAdmin)




