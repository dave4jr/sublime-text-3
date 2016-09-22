#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 urls.py
#*====================== #
from django.conf.urls import url
from . import views


# ==================================================#
#	Main
# ==================================================#
urlpatterns = [
	url(r'^$', views.main, {"template":"index.html"}, name="index"),

]


