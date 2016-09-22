#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 urls.py
#*====================== #
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf import settings
from . import views
admin.autodiscover()

admin.site.site_header = 'BrundageSmith'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Clients'



#	Main
# ========================================= #
urlpatterns = [
	url(r'^buy/$', views.buy, {"template":"buy.html"}, name="buy"),
	url(r'^buy/(?P<listing_rid>\d+)/$', views.buy_single, {"template":"buy-single.html"}, name="buy-single"),
]








	

