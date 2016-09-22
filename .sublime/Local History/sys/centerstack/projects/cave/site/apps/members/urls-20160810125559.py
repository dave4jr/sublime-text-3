#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 members/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as member_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', member_views.main, {"template":"members.html"}, name="members"),
	url(r'^edit/(?P<pk>\d+)/$', member_views.edit, {"template":"include/modal-members.html"}, name='edit_member'),
]






