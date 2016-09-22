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
	url(r'^sudo/', include('sudo.urls')),
]


#	Main
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^sell/$', views.main, {"template":"sell.html"}, name="sell"),
	url(r'^about/$', views.main, {"template":"about.html"}, name="about"),
	url(r'^neighborhoods/$', views.main, {"template":"neighborhoods.html"}, name="neighborhoods"),
	url(r'^404/$', views.main, {"template":"404.html"}, name="404"),
	url(r'^admin/$', views.admin, name="admin"),
]


#	Featured
# ====================================== #
# urlpatterns += [
# 	url(r'^bend-trend-homes/$', views.main, {"template":"index.html"}, name="index"),
# ]








	

