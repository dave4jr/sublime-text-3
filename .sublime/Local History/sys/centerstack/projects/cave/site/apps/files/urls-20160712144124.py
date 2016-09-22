#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 customers/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', views.main, {"template":"files.html"}, name='files'),
	url(r'^new_folder/$', views.new_folder, {"template":"files.html"}, name='files_new_folder'),
	# url(r'^delete/$', views.delete, {"template":"files.html"}, name='files_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





