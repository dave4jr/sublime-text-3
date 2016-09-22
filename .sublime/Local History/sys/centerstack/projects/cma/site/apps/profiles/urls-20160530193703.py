#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 profiles/urls.py
#*========================== #
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^users/$', views.main, {"template":"users.html"}, name="users"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




