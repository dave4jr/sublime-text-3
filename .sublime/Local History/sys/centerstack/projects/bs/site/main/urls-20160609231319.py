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
	url(r'^$', views.main, {"template":"base.html"}, name="index"),
	url(r'^home/$', views.main, {"template":"index.html"}, name="index"),
	url(r'^sell/$', views.main, {"template":"base.html"}, name="sell"),
	url(r'^about/$', views.main, {"template":"base.html"}, name="about"),
	url(r'^contact/$', views.main, {"template":"base.html"}, name="contact"),
	url(r'^neighborhoods/$', views.main, {"template":"base.html"}, name="neighborhoods"),
	url(r'^listings/$', views.main, {"template":"base.html"}, name="listings"),
	url(r'^detail/$', views.main, {"template":"base.html"}, name="detail"),
	url(r'^403/$', views.main, {"template":"base.html"}, name="403"),
	url(r'^404/$', views.main, {"template":"base.html"}, name="404"),
	url(r'^500/$', views.main, {"template":"base.html"}, name="500"),
	url(r'^admin/$', views.admin, name="admin"),
]








	

