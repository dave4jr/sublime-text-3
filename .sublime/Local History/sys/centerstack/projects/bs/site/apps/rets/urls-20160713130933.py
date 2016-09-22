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
	url(r'^buy2/$', views.buy, {"template":"buy2.html"}, name="buy2"),
	url(r'^buy3/$', views.buy, {"template":"buy3.html"}, name="buy3"),
	url(r'^buy/(?P<pk>\d+)/$', views.buy_single, {"template":"buy-single.html"}, name="buy-single"),
	url(r'^listings/$', views.listings, {"template":"listings.html"}, name="listings"),
	url(r'^featured/$', views.listings, {"template":"featured.html"}, name="featured"),
]








	

