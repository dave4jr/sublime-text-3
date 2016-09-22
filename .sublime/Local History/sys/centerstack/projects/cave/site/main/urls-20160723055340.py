#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 urls.py
#*====================== #
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
admin.site.login = login_required(admin.site.login)
admin.autodiscover()

admin.site.site_header = 'DIYcave'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Models'


# ==================================================#
#	 Login / Logout
# ==================================================#
urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
	url(r'^logout/$', auth_views.logout, {"next_page": "login.html"}, name="logout"),
	url(r'^admin/logout/$', auth_views.logout, {"next_page": "login"}, name="logout"),
]



# ==================================================#
#	3rd Party
# ==================================================#
urlpatterns += [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^session_security/', include('session_security.urls')),
	url(r'^tinymce/', include('tinymce.urls')),
]


# ==================================================#
#	My Applications
# ==================================================#
urlpatterns += [
	url(r'^members/', include('members.urls')),
	url(r'^classes/', include('classes.urls')),
	url(r'^inventory/', include('inventory.urls')),
]



# ==================================================#
#	Main
# ==================================================#
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^calendar/$', views.main, {"template":"calendar.html"}, name="calendar"),
	url(r'^pos/$', views.main, {"template":"pos.html"}, name="pos"),
	url(r'^charge/$', views.main, {"template":"charge2.html"}, name="charge"),

]


# ==================================================#
#	Dropdowns
# ==================================================#
urlpatterns += [
	url(r'^dropdowns/$', views.dropdowns, {"template":"dropdowns.html"}, name="dropdowns"),
	url(r'^dropdowns/level/new/$', views.dropdown_level_new, {"template":"dropdowns.html"}, name="dropdown_level_new"),
	url(r'^dropdowns/level/delete/$', views.dropdown_level_delete, {"template":"dropdowns.html"}, name="dropdown_level_delete"),
]


# ==================================================#
#	Admin
# ==================================================#
urlpatterns += [
	url(r'^admin/$', views.admin, name="admin"),
	url(r'^admin/auth/group/$', views.main, name="groups"),
	url(r'^admin/auth/user/$', views.main, name="users"),
	url(r'^admin/auth/user/add/$', views.main, name="new-user-admin"),
	url(r'^admin/auth/group/add/$', views.main, name="new-group"),
]







# ==================================================#
#	Debug Toolbar / Static
# ==================================================#
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



	

