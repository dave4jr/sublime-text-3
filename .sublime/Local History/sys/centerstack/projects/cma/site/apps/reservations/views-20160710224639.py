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
from customers.models import Customer
from preferences.models import Preference
from .forms import CheckoutForm
from .forms import CheckinForm
from .forms import ReservationForm
from .forms import CheckoutConditionForm
from .forms import CheckoutMembershipForm
from .forms import CheckoutLiabilityForm
from bikes.models import Bike
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
def checkout(request, template):
	try:
		customer_id = request.POST.getlist('customer')[0]
		reservation_id = Reservation.objects.filter(customer__id=customer_id).values_list('id', flat=True)
		reservation = Reservation.objects.get(id=reservation_id)
	except:
		return redirect("index")

	print request.method

	if request.method == "POST":
		form = CheckoutForm(request.POST, instance=reservation, initial={"checkout_mileage": reservation.bike.current_mileage, "checkout_datetime_actual": reservation.checkout_datetime, "checkout_notes": reservation.notes })
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
#	Main
# ==================================================#
def checkout_agreement_forms(request, template, pk):
	reservation = Reservation.objects.get(pk=pk)
	if request.POST == "POST":
		a_valid = formA.is_valid()
		b_valid = formB.is_valid()
		c_valid = formC.is_valid()
		if a_valid and b_valid and c_valid:
			a = formA.save()
			b = formB.save(commit=False)
			c = formC.save(commit=False)
			b.foreignkeytoA = a
			b.save()
			c.foreignkeytoB = b
			c.save()
		
	else:
		form = ReservationForm(instance=reservation)
	return render(request, template, {"reservation":reservation, "ReservationForm": form } )





# ==================================================#
#	Check-In
# ==================================================#
def checkin(request, template):
	customer_id = request.POST.getlist('customer')[0]
	bike_id = request.POST.getlist('bike')[0]

	if len(customer_id) != 0:
		reservation_id = Reservation.objects.filter(customer__id=customer_id).values_list('id', flat=True)
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












