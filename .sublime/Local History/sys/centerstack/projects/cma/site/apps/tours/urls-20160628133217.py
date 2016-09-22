#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 tours/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as tour_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', tour_views.main, {"template":"tours.html"}, name="tours"),
	url(r'^new/$', tour_views.main, {"template":"edit/tour_form.html"}, name="tour_new"),
	url(r'^delete/$', tour_views.delete, {"template":"tours.html"}, name="tour_delete"),
	url(r'^edit/(?P<pk>\d+)/$', tour_views.edit, {"template":"edit/tour_form.html"}, name='tour_edit'),
]





