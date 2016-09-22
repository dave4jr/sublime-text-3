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
	url(r'^new/$', reservation_views.main, {"template":"edit/reservation_form.html"}, name="reservation_new"),
	url(r'^delete/$', reservation_views.delete, {"template":"reservations.html"}, name="reservation_delete"),
	url(r'^edit/(?P<pk>\d+)/$', reservation_views.edit, {"template":"edit/reservation_form.html"}, name='reservation_edit'),
]

# ==================================================#
#	Processing
# ==================================================#
urlpatterns += [
	url(r'^checkout/$', reservation_views.checkout, {"template":"checkout.html"}, name="checkout"),
	url(r'^checkin/$', reservation_views.checkin, {"template":"checkin.html"}, name="checkin"),
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














