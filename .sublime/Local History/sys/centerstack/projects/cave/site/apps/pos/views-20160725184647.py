#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/views.py
#*========================== #
from django.shortcuts import render, redirect
from django.http import HttpResponse
import stripe, logging, json
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
			data = {"response": "approved" }
		except stripe.error.CardError as e:
			data = {"response": "declined", "error": e }

		return HttpResponse(json.dumps(data), 'application/json')
	



def pos(request, template):
	return render(request, template)

 
