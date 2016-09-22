#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	reservations/views.py
#*======================== #
from django.shortcuts import render, redirect
from django.http import  HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django_xworkflows.xworkflow_log.models import TransitionLog
from .models import Reservation
from members.models import Member
from preferences.models import Preference
from .forms import CheckoutForm
from .forms import CheckinForm
from .forms import ReservationForm
from .forms import CheckoutConditionForm
from .forms import CheckoutMembershipForm
from .forms import CheckoutLiabilityForm
from bikes.models import Bike
from bikes.forms import BikeForm
from tours.models import Tour
import logging, sys


# ==================================================#
#	Main
# ==================================================#
def main(request, template):
	reservations = Reservation.objects.all()
	if request.method == "POST":
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('reservations')
	else:
		form = ReservationForm()
	return render(request, template, {"reservations":reservations, "ReservationForm": form } )



# ==================================================#
#	Edit
# ==================================================#
def edit(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)
	preference = Preference.objects.get(pk=1)
	if request.method == "POST":
		form = ReservationForm(request.POST, instance=reservation)
		if form.is_valid():
			try:
				pk = list(request.POST.getlist('delete'))[0]
				Reservation.objects.get(pk=pk).delete()
				return redirect('reservations')
			except:
				form.save()
				return redirect('reservations')
	else:
		form = ReservationForm(instance=reservation)
	return render(request, template, {"reservation":reservation, "preference":preference, "ReservationForm": form } )



# ==================================================#
#	Checkout
# ==================================================#
def checkout(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)

	if request.method == "POST":
		form = CheckoutForm(request.POST, instance=reservation)
		if form.is_valid():
			form.save
			return redirect("checkout")
	else:
		form = CheckoutForm(instance=reservation, initial={"checkout_mileage": reservation.bike.current_mileage, "checkout_datetime_actual": reservation.checkout_datetime, "checkout_notes": reservation.notes })

	context = {
		"CheckoutForm": form,
		"reservation":reservation,
	}
	return render(request, template, context)



# ==================================================#
#	Checkout Condition / Membership / Liability
# ==================================================#
def checkout_condition(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)
	bike = Bike.objects.get(pk=reservation.bike.pk)

	if request.method == "POST":
		checkout_condition_form = CheckoutConditionForm(request.POST, instance=reservation)
		bike_form = BikeForm(request.POST, instance=bike)
		if checkout_condition_form.is_valid() and bike_form.is_valid():
			checkout_condition_form.save()
			bike_form.save()
			return redirect("checkout", pk=pk)
	else:
		checkout_condition_form = CheckoutConditionForm(instance=reservation, initial={"checkout_datetime_actual": reservation.checkout_datetime, "checkin_datetime_actual": reservation.checkin_datetime })
		bike_form = BikeForm(instance=bike)
		
	return render(request, template, {"reservation":reservation, "CheckoutConditionForm": checkout_condition_form, "BikeForm":bike_form } )


def checkout_membership(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)

	if request.method == "POST":
		form = CheckoutMembershipForm(request.POST, instance=reservation)
		if form.is_valid():
			form.save()
			return redirect("checkout", pk=pk)
	else:
		form = CheckoutMembershipForm(instance=reservation)
		
	return render(request, template, {"reservation":reservation, "CheckoutMembershipForm": form } )


def checkout_liability(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)

	if request.method == "POST":
		form = CheckoutLiabilityForm(request.POST, instance=reservation)
		if form.is_valid():
			form.save()
			return redirect("checkout", pk=pk)
	else:
		form = CheckoutLiabilityForm(instance=reservation)

	return render(request, template, {"reservation":reservation, "CheckoutLiabilityForm": form } )





# ==================================================#
#	Check-In
# ==================================================#
def checkin(request, template):
	member_id = request.POST.getlist('member')[0]
	bike_id = request.POST.getlist('bike')[0]

	if len(member_id) != 0:
		reservation_id = Reservation.objects.filter(member__id=member_id).values_list('id', flat=True)
	else:
		reservation_id = Reservation.objects.filter(bike__id=bike_id).values_list('id', flat=True)
	
	reservation = Reservation.objects.get(id=reservation_id)

	if request.method == "POST":
		form = CheckinForm(request.POST, instance=reservation)
		if form.is_valid():
			form.save
			logging.debug("Saved")
			return redirect("checkin")
	else:
		form = CheckinForm(instance=reservation)

	context = {
		"CheckinForm": form,
		"reservation":reservation,
	}
	return render(request, template, context)


# ==================================================#
#	Delete Checked
# ==================================================#
def delete(request, template):
	if request.method == "POST":
		name = list(request.POST.getlist('checked'))
		for ii in name:
			Reservation.objects.get(pk=ii).delete()
		del name[:]
		return redirect('reservations')
	return render(request, template)


# ==================================================#
#	Invoice View
# ==================================================#
def invoice(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)
	return render(request, template, {'reservation': reservation})



# ==================================================#
#	Email View
# ==================================================#
def email(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)
	bike = Bike.objects.get(pk=pk)
	return render(request, template, {'reservation': reservation, 'bike': bike})



# ==================================================#
#	Stripe
# ==================================================#












