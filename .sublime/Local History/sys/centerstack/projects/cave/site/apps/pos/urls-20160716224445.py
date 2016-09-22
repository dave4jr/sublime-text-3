#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/urls.py
#*========================== #
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import views as pos_views
 

urlpatterns = [
	url(r'^$', pos_views.main, {"template":"pos.html"}, name="pos"),
]




