#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 customs/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as custom_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', custom_views.main, {"template":"customs.html"}, name="customs"),
	url(r'^new/$', custom_views.main, {"template":"edit/custom_form.html"}, name="custom_new"),
	url(r'^delete/$', custom_views.delete, {"template":"customs.html"}, name="custom_delete"),
	url(r'^edit/(?P<pk>\d+)/$', custom_views.edit, {"template":"edit/custom_form.html"}, name='custom_edit'),
]





