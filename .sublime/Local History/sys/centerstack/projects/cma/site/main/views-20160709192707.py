#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 main/views.py
#*====================== #
import os
import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.template import RequestContext
from reservations.models import Reservation
from reservations.models import Search
from reservations.forms import ReservationForm
from preferences.models import Preference
from preferences.forms import PreferenceForm
from reservations.forms import CheckoutForm
from reservations.forms import CheckinForm
from reservations.forms import AvailabilityForm
from bikes.models import Bike
from django_xworkflows.xworkflow_log.models import TransitionLog
from datetime import datetime



#	Main View
# ========================= #
def main(request, template):
	reservations = Reservation.objects.all()
	bikes = Bike.objects.all()
	logs = TransitionLog.objects.all()
	preference = Preference.objects.get(pk=1)
	checkoutform = CheckoutForm()
	checkinform = CheckinForm()
	check_availability_form = AvailabilityForm()
	context = {
		"reservations":reservations,
		"logs":logs,
		"bikes":bikes,
		"CheckoutForm":checkoutform,
		"CheckinForm":checkinform,
		"AvailabilityForm":check_availability_form,
		"preference": preference,
	}
	return render(request, template, context)




#	Admin
# ====================================== #
@login_required
def admin(request):
	context = {}
	return render(request, context)



# ====================================== #
#	Workflow
# ====================================== #
def workflow(request, template, fn):
	if request.method == "POST":
		reservation_pk = request.POST.getlist('pk')[0]
		reservation = Reservation.objects.get(pk=reservation_pk)
		
		if fn == "checkin":
			form = CheckinForm(request.POST, instance=reservation)
		elif fn == "checkout":
			form = CheckoutForm(request.POST, instance=reservation)

		form.save
		state = reservation.status

		if fn == "checkout":
			reservation.checkout()
		elif fn == "checkin":
			reservation.checkin_no_damage()
		elif fn == "reveive_damage_payment":
			reservation.receive_damage_payment()
		elif fn == "reset":
			reservation.status = "pending_deposit"
		return redirect('reservations')
	return render(request, template, {"reservation": reservation})



# ====================================== #
#	Workflow (Pk & fn)
# ====================================== #
def workflow_pk(request, template, pk, fn):
	if request.method == "POST":
		reservation = Reservation.objects.get(pk=pk)
		state = reservation.status

		if fn == "receive_deposit":
			reservation.receive_deposit()
		elif fn == "checkout":
			reservation.checkout()
		elif fn == "checkin":
			reservation.checkin()
		elif fn == "no_damage":
			reservation.no_damage()
		elif fn == "damage":
			reservation.damage()
		elif fn == "send_damage_invoice":
			send_damage_invoice()
		elif fn == "reveive_damage_payment":
			reservation.receive_damage_payment()
		elif fn == "reset":
			reservation.status = "pending_deposit"

		return redirect('index')
	return render(request, template, {"reservation": reservation})


#	Check Availability
# ====================================== #
search = []
def availability(request, template):

	reservations = Reservation.objects.all()
	logs = TransitionLog.objects.all()
	checkoutform = CheckoutForm()
	checkinform = CheckinForm()
	check_availability_form = AvailabilityForm()

	if request.method == "POST":
		start = request.POST['start']
		end = request.POST['end']

		#	Converting to Datetime
		# ====================================== #
		start = datetime.strptime(start, "%m/%d/%Y - %I:%M%p")
		end = datetime.strptime(end, "%m/%d/%Y - %I:%M%p")

		for reservation in reservations:
			if (start < end < reservation.checkout_datetime) or (end > start > reservation.checkin_datetime):
				search.append("%s: Available" % reservation.bike)
			elif (start < end < reservation.checkout_datetime):
				search.append("%s: Check-Out: OK | Check-In: | %s" % (reservation.bike, reservation.checkin_datetime))
			elif (end < reservation.checkin_datetime):
				search.append("%s: Check-In: OK | Check-Out: | %s" % (reservation.bike, reservation.checkout_datetime))
			else:
				search.append("%s: Unavailable" % reservation.bike)

		context = {
			"reservations":reservations,
			"logs":logs,
			"CheckoutForm":checkoutform,
			"CheckinForm":checkinform,
			"AvailabilityForm":check_availability_form,
			"searches":search,
		}

		return render(request, template, context)






