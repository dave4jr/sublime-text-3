#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/urls.py
#*========================== #
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import views
 

urlpatterns = [
	url(r'^$', views.pos, {"template":"pos.html"}, name="pos"),
]




