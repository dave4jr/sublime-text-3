#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	tours/admin.py
#*======================== #
from django.contrib import admin
from .models import Tour
from .models import Guide
from .models import Location
from .models import Tour
from .models import TourAccessories
from .models import BikePrice
from bikes.models import Bike
import logging


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
	list_display = ("name",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = ("name",)


@admin.register(TourAccessories)
class TourAccessoriesAdmin(admin.ModelAdmin):
	list_display = ("name","price", "price_period")


#	Inlines
# ========================= #
class BikePriceInline(admin.StackedInline):
	model = BikePrice
	show_change_link = True
	verbose_name = "Tour"
	extra = 0



class TourAdmin(admin.ModelAdmin):
	list_display 			= ('id', 'name', 'date_start', 'date_end', 'duration', 'location', 'guide', 'skill', 'milage', 'price_shared', 'price_single', 'deposit')
	ordering 			= ("name",)
	list_display_links 		= ("name",)
	save_as 			= True
	inlines			= [ BikePriceInline ]
admin.site.register(Tour, TourAdmin)

