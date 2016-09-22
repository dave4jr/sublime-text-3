#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 calendar/urls.py
#*========================== #
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from . import views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', views.main, {"template":"calendar.html"}, name="calendar"),
	url(r'^new/$', views.main, {"template":"edit/calendar_form.html"}, name="calendar_new"),
	url(r'^delete/$', views.delete, {"template":"calendar.html"}, name="calendar_delete"),
	url(r'^edit/(?P<pk>\d+)/$', views.edit, {"template":"edit/calendar_form.html"}, name='calendar_edit'),
]




