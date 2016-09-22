#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 reservation/urls.py
#*========================== #
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from . import views as reservation_views
admin.autodiscover()

# ==================================================#
#	Applications
# ==================================================#
urlpatterns = [
	url(r'^$', reservation_views.main, {"template":"reservations.html"}, name="reservations"),
	url(r'^new/$', reservation_views.main, {"template":"edit/reservation_new.html"}, name="reservation_new"),
	url(r'^delete/$', reservation_views.delete, {"template":"reservations.html"}, name="reservation_delete"),
	url(r'^edit/(?P<pk>\d+)/$', reservation_views.edit, {"template":"edit/reservation_form.html"}, name='reservation_edit'),
]


# ==================================================#
#	Processing
# ==================================================#
urlpatterns += [
	url(r'^checkout/(?P<pk>\d+)/$', reservation_views.checkout, {"template":"processing/checkout.html"}, name="checkout"),
	url(r'^checkin/(?P<pk>\d+)/$', reservation_views.checkin, {"template":"processing/checkin.html"}, name="checkin"),
	
	url(r'^checkout_condition/(?P<pk>\d+)/$', reservation_views.checkout_condition, {"template":"processing/checkout_condition.html"}, name="checkout_condition"),
	url(r'^checkout_membership/(?P<pk>\d+)/$', reservation_views.checkout_membership, {"template":"processing/checkout_membership.html"}, name="checkout_membership"),
	url(r'^checkout_liability/(?P<pk>\d+)/$', reservation_views.checkout_liability, {"template":"processing/checkout_liability.html"}, name="checkout_liability"),
]


# ==================================================#
#	Emails
# ==================================================#
urlpatterns += [
	url(r'^email/confirmation/$', reservation_views.main, {"template":"email/confirmation.html"}, name="email_confirmation"),
	url(r'^email/reminder/$', reservation_views.main, {"template":"email/reminder.html"}, name="email_reminder"),
	url(r'^email/thankyou/$', reservation_views.main, {"template":"email/thankyou.html"}, name="email_thankyou"),
	url(r'^email/confirmation/(?P<pk>\d+)/$', reservation_views.email, {"template":"email/confirmation.html"}, name='email_send_confirmation'),
]















