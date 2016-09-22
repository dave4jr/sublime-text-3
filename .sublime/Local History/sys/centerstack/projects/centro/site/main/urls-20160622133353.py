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
]


#	Structure
# ========================================= #
urlpatterns += [
	url(r'^admin/$', views.admin, name="admin"),
]


#	Main
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^about/$', views.main, {"template":"base.html"}, name="about"),
	url(r'^products/$', views.main, {"template":"base.html"}, name="products"),
	url(r'^services/$', views.main, {"template":"base.html"}, name="services"),
	url(r'^testimonials/$', views.main, {"template":"testimonials.html"}, name="testimonials"),
	url(r'^contact/$', views.main, {"template":"contact.html"}, name="contact"),
]




#	Debug Toolbar
# ====================================== #
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




	

