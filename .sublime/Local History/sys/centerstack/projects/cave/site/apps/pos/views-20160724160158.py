#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/views.py
#*========================== #
from django.shortcuts import render, redirect
import stripe, logging
from django.conf import settings
from members.models import Member




#	Charge
# ====================================== #
def charge(request, template):
	if request.method == "POST":
		stripe.api_key = settings.STRIPE_SECRET_KEY
		token = request.POST.get('token', '')
		try:
			amount = 1000
			charge = stripe.Charge.create(amount=amount, currency="usd", source=token, description="Testing Charge")
		except stripe.error.CardError as e:
			print e
	return render(request, template)




def pos(request, template):
	return render(request, template)

 
