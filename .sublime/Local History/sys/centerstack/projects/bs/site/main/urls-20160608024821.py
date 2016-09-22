#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 urls.py
#*====================== #
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
admin.autodiscover()

admin.site.site_header = 'BrundageSmith'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Clients'


#	Applications
# ========================================= #
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^interface/', include('interface.urls')),
	url(r'^rets/', include('rets.urls')),
	url(r'^villareal/', include('villareal.urls')),
	url(r'^sudo/', include('sudo.urls')),
]


#	Main
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^sell/$', views.main, {"template":"sell.html"}, name="sell"),
	url(r'^about/$', views.main, {"template":"about.html"}, name="about"),
	url(r'^contact/$', views.main, {"template":"contact.html"}, name="contact"),
	url(r'^neighborhoods/$', views.main, {"template":"neighborhoods.html"}, name="neighborhoods"),
	url(r'^listings/$', views.main, {"template":"listings.html"}, name="listings"),
	url(r'^detail/$', views.main, {"template":"index.html"}, name="detail"),
	url(r'^403/$', views.main, {"template":"403.html"}, name="403"),
	url(r'^404/$', views.main, {"template":"404.html"}, name="404"),
	url(r'^500/$', views.main, {"template":"500.html"}, name="500"),
	url(r'^admin/$', views.admin, name="admin"),
]








	

