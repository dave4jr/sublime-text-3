#*========================= #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 partners/urls.py
#*========================= #
from django.conf.urls import url, include
from django.contrib import admin
from . import views
admin.autodiscover()


#	Blog
# ========================================= #
urlpatterns = [
	url(r'^$', views.main, {"template":"partners.html"}, name="partners"),
	url(r'^(?P<pk>\d+)/$', views.partners_single, {"template":"partners-single.html"}, name="partners-single"),
]

	

