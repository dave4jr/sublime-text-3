#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 inventory/urls.py
#*========================== #
from django.conf.urls import url, include
from django.contrib import admin
from . import views as inventory_views
admin.autodiscover()

# ==================================================#
#	Inventory URLS
# ==================================================#
urlpatterns = [
	url(r'^$', inventory_views.main, {"template":"inventory.html"}, name="inventory"),
	url(r'^new/$', inventory_views.main, {"template":"edit/inventory_edit.html"}, name="inventory_new"),
	url(r'^delete/$', inventory_views.delete, {"template":"inventory.html"}, name="inventory_delete"),
	url(r'^edit/(?P<pk>\d+)/$', inventory_views.edit, {"template":"edit/inventory_edit.html"}, name='inventory_edit'),
]




