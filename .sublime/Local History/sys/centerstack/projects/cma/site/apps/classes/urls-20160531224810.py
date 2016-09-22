#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 classes/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as class_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', class_views.main, {"template":"classes.html"}, name="classes"),
	url(r'^new/$', class_views.main, {"template":"edit/class_form.html"}, name="class_new"),
	url(r'^delete/$', class_views.delete, {"template":"classes.html"}, name="class_delete"),
	url(r'^edit/(?P<pk>\d+)/$', class_views.edit, {"template":"edit/class_form.html"}, name='class_edit'),
]




