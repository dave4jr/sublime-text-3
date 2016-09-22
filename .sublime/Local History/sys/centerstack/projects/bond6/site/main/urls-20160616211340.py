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

admin.site.site_header = 'Bond6 Fitness'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Clients'


#	Includes
# ========================================= #
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^massive/', include('massive.urls')),
	url(r'^sudo/', include('sudo.urls')),
]


#	Structure
# ========================================= #
urlpatterns += [
	# url(r'^404/$', views.main, {"template":"404.html"}, name="404"),
	url(r'^admin/$', views.admin, name="admin"),
]


#	Main
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^what-we-do/$', views.main, {"template":"what-we-do.html"}, name="what-we-do"),
	url(r'^train-with-us/$', views.main, {"template":"base.html"}, name="train-with-us"),
	url(r'^refer-a-friend/$', views.main, {"template":"base.html"}, name="refer-a-friend"),
	url(r'^testimonials/$', views.main, {"template":"base.html"}, name="testimonials"),
	url(r'^blog/$', views.main, {"template":"base.html"}, name="blog"),
	url(r'^contact/$', views.main, {"template":"base.html"}, name="contact"),
]




#	Debug Toolbar
# ====================================== #
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




	

