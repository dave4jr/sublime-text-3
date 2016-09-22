#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/admin.py
#*========================== #
from django.contrib import admin
from .models import RetsData
from .models import Property


#	RetsData
# ====================================== #
class RetsDataAdmin(admin.ModelAdmin):
	list_display 			= ("id", "update", "json")
	ordering 			= ("update",)
admin.site.register(RetsData, RetsDataAdmin)


#	Property
# ====================================== #
class PropertyAdmin(admin.ModelAdmin):
	list_display 			= ("id", "acres","area","bathrooms","bedrooms","city","county","latitude","listingagentfullname","listingdate","listingprice","listingrid","longitude","mlnumber","propertytype","region","resiexte","resihoa","resihoad","resihoap","resihtco","resiinc1","resiinc2","resiinc3","resiinte","resikitc","resilevl","resipark","resiroom","resistyl","resiview","resiwtrd","squarefootage","state","status","statusdate","streetname","streetnumber","streetsuffix","style","unit","yearbuilt","zipcode")
	ordering 			= ("id",)
admin.site.register(Property, PropertyAdmin)




