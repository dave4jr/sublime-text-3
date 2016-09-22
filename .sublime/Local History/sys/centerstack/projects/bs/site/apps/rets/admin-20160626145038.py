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
	list_display 			= ("id", "property_id", "acres","area","bathrooms","bedrooms","city","resicomm","county","resiexte","resihtco","resihoa","resihoap","resihoad","resiinc1","resiinc2","resiinc3","resiinte","resikitc","latitude","listingagentfullname","listingdate","mlnumber","listingprice","listingrid","longitude","marketingremarks","resipark","propertytype","region","resiroom","style","squarefootage","state","status","statusdate","streetname","streetnumber","streetsuffix","resistyl","unit","resiview","yearbuilt","zipcode","resiwtrd","resilevl")
	ordering 			= ("id",)
admin.site.register(Property, PropertyAdmin)




