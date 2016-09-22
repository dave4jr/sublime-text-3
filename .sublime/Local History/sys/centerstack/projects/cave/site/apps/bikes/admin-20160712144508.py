#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	bikes.admin.py
#*======================== #
from django.contrib import admin
from .models import Bike
from .models import Color
from .models import Manufacturer
from .models import Accessories





admin.site.register(Bike)
admin.site.register(Color)
admin.site.register(Manufacturer)
admin.site.register(Accessories)
















	


