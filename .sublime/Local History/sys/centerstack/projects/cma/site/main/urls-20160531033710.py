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

admin.site.site_header = 'Colorado Motorcycle Adventures'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Models'

# ==================================================#
#	Admin / 3rd Party
# ==================================================#
urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^session_security/', include('session_security.urls')),
]


# ==================================================#
#	My Applications
# ==================================================#
urlpatterns += [
	url(r'^reservations/', include('reservations.urls')),
	url(r'^tours/', include('tours.urls')),
	url(r'^customers/', include('customers.urls')),
	url(r'^bikes/', include('bikes.urls')),
	url(r'^classes/', include('classes.urls')),
	url(r'^files/', include('files.urls')),
	url(r'^preferences/', include('preferences.urls')),
	url(r'^profiles/', include('profiles.urls')),
]


# ==================================================#
#	Availability / Workflow / Processing
# ==================================================#
urlpatterns += [
	url(r'^availability/$', views.availability, {"template":"index.html"}, name="availability"),
	url(r'^workflow/(?P<fn>\w+)/$', views.workflow, {"template":"index.html"}, name="workflow"),
	url(r'^workflow/(?P<pk>\d+)/(?P<fn>\w+)/$', views.workflow_pk, {"template":"index.html"}, name="workflow_pk"),
]



# ==================================================#
#	Main
# ==================================================#
urlpatterns += [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),
	url(r'^calendar/$', views.main, {"template":"calendar.html"}, name="calendar"),

]


# ==================================================#
#	Add
# ==================================================#
urlpatterns += [
	url(r'^bike_accessory_add/$', views.main, {"template":"bike_accessory_add.html"}, name="bike_accessory_add"),
	url(r'^group_add/$', views.main, {"template":"group_add.html"}, name="group_add"),
	url(r'^location_add/$', views.main, {"template":"location_add.html"}, name="location_add"),
	url(r'^storage_accessories_add/$', views.main, {"template":"storage_accessories_add.html"}, name="storage_accessories_add"),
	url(r'^tour_accessories_add/$', views.main, {"template":"tour_accessories_add.html"}, name="tour_accessories_add"),

]


# ==================================================#
#	Admin
# ==================================================#
urlpatterns += [
	url(r'^admin/$', views.admin, name="admin"),
	url(r'^admin/auth/group/$', views.main, name="groups"),
	url(r'^admin/auth/user/$', views.main, name="users-admin"),
	url(r'^admin/auth/user/add/$', views.main, name="new-user-admin"),
	url(r'^admin/auth/group/add/$', views.main, name="new-group"),
]



# ==================================================#
#	 Login / Logout
# ==================================================#
urlpatterns += [
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
	url(r'^logout/$', auth_views.logout, {"next_page": "/"}, name="logout"),
]





# ==================================================#
#	Debug Toolbar / Static
# ==================================================#
if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^debug/', include(debug_toolbar.urls)),
	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



	

