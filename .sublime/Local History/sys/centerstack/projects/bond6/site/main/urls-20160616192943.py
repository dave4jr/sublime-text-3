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
	url(r'^403/$', views.main, {"template":"403.html"}, name="403"),
	url(r'^404/$', views.main, {"template":"404.html"}, name="404"),
	url(r'^500/$', views.main, {"template":"500.html"}, name="500"),
	url(r'^admin/$', views.admin, name="admin"),
]


#	Main
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^about/$', views.main, {"template":"about.html"}, name="about"),
	url(r'^fitness/$', views.main, {"template":"index.html"}, name="fitness"),
	url(r'^gallery/$', views.main, {"template":"gallery.html"}, name="gallery"),
	url(r'^exercises/$', views.main, {"template":"exercises.html"}, name="exercises"),
	url(r'^testimonials/$', views.main, {"template":"testimonials.html"}, name="testimonials"),
	url(r'^blog/$', views.main, {"template":"blog.html"}, name="blog"),
	url(r'^blog-single/$', views.main, {"template":"blog-single.html"}, name="blog-single"),
	url(r'^contact/$', views.main, {"template":"contact.html"}, name="contact"),
]




#	Debug Toolbar
# ====================================== #
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




	

