#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 inventory/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as bike_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', bike_views.main, {"template":"inventory.html"}, name="inventory"),
	url(r'^new/$', bike_views.main, {"template":"edit/bike_new.html"}, name="bike_new"),
	url(r'^delete/$', bike_views.delete, {"template":"inventory.html"}, name="bike_delete"),
	url(r'^edit/(?P<pk>\d+)/$', bike_views.edit, {"template":"edit/bike_form.html"}, name='bike_edit'),
]




