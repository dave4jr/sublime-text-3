#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 customers/urls.py
#*========================== #
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from . import views as customer_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', customer_views.main, {"template":"customers.html"}, name="customers"),
	url(r'^new/$', customer_views.main, {"template":"edit/customer_form.html"}, name="customer_new"),
	url(r'^delete/$', customer_views.delete, {"template":"customers.html"}, name="customer_delete"),
	url(r'^edit/(?P<pk>\d+)/$', customer_views.edit, {"template":"edit/customer_form.html"}, name='customer_edit'),
]




