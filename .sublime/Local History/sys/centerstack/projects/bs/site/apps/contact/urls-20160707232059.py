#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 contact/urls.py
#*====================== #
from django.conf.urls import patterns, url, include
from django.contrib import admin
from . import views as contact_views
admin.autodiscover()


#	Blog
# ========================================= #
urlpatterns = [
	url(r'^$', contact_views.main, {"template":"contact.html"}, name="contact"),
]

	

