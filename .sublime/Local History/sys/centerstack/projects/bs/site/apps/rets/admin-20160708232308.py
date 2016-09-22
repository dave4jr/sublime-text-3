#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/admin.py
#*========================== #
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import Property



#	Property
# ====================================== #
class PropertyAdmin(ImportExportModelAdmin):
	list_display 			= ("id","property_id","keysearch","acres","bathrooms","bedrooms","city","county","latitude","listingagentfullname","listingdate","listingprice","listingrid","longitude","mlnumber","propertytype","resiexte","resihoa","resihoad","resihoap","resihtco","resiinc1","resiinc2","resiinc3","resiinte","resikitc","resilevl","resipark","resiroom","resistyl","resiview","resiwtrd","squarefootage","state","status","statusdate","streetname","streetnumber","streetsuffix","style","unit","yearbuilt","zipcode")
	ordering 			= ("id",)
admin.site.register(Property, PropertyAdmin)



#	Property Import Resource
# ====================================== #
# class PropertyResource(resources.ModelResource):
#     	class Meta:
#         	model = Property
#         	fields = ("id","property_id","keysearch","acres","bathrooms","bedrooms","city","county","latitude","listingagentfullname","listingdate","listingprice","listingrid","longitude","mlnumber","propertytype","resiexte","resihoa","resihoad","resihoap","resihtco","resiinc1","resiinc2","resiinc3","resiinte","resikitc","resilevl","resipark","resiroom","resistyl","resiview","resiwtrd","squarefootage","state","status","statusdate","streetname","streetnumber","streetsuffix","style","unit","yearbuilt","zipcode")






