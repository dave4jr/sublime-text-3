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

admin.site.site_header = 'CenterStack'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Clients'


#	Applications
# ========================================= #
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^session_security/', include('session_security.urls')),
	url(r'^aura/', include('aura.urls')),
	url(r'^blog/', include('blog.urls')),
	url(r'^planner/', include('planner.urls')),
	url(r'^contact/', include('contact.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
]


#	Basic Pages
# ========================================= #
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^about/$', views.main, {"template":"about.html"}, name="about"),
	url(r'^portfolio/$', views.main, {"template":"portfolio.html"}, name="portfolio"),
	url(r'^terms-of-use/$', views.main, {"template":"terms-of-use.html"}, name="terms-of-use"),
	url(r'^newsletter/$', views.main, {"template":"newsletter.html"}, name="newsletter"),
	url(r'^404/$', views.main, {"template":"404.html"}, name="404"),
	url(r'^500/$', views.main, {"template":"500.html"}, name="500"),
	url(r'^admin/$', views.admin, name="admin"),
]


#	Account Login
# ========================================= #
urlpatterns += [
	url(r'^login/$', auth_views.login, {"template_name": "login.html"}, name="login"),
	url(r'^logout/$', auth_views.logout, {"next_page": "/"}, name="logout"),
	url(r'^change-password/$', auth_views.password_change, name="password_change"),
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




	

