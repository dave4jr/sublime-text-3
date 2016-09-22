#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 contact/urls.py
#*====================== #
from django.conf.urls import url, include
from django.contrib import admin
from . import views
admin.autodiscover()


#	Blog
# ========================================= #
urlpatterns = [
	# url(r'^$', views.main, {"template":"contact.html"}, name="contact"),
]

	

