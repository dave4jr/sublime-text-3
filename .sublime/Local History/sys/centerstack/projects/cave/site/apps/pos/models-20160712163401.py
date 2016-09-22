#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments.py
#*========================== #
from django.db import models
from django.conf import settings
from preferences.models import Preference
import stripe
 

class Payment(models.Model):
	
	def __init__(self, *args, **kwargs):
		super(Payment, self).__init__(*args, **kwargs)
		stripe.api_key = settings.STRIPE_SECRET_KEY
		self.stripe = stripe

	charge_id = models.CharField(max_length=32)
 

	def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
 
		if self.charge_id:
			return False, Exception(message="Already Charged.")
		try:
			response = self.stripe.Charge.create(
				amount = price_in_cents,
				currency = "usd",
				card = {
					"number" : number,
					"exp_month" : exp_month,
					"exp_year" : exp_year,
					"cvc" : cvc,
				},
				description='Thank you For Trusting Us With Your Motorcycle Needs!')
			self.charge_id = response.id
			
		except self.stripe.CardError, ce:
			return False, ce
		return True, response



class Plan(models.Model):
	def __init__(self, *args, **kwargs):
		super(Plan, self).__init__(*args, **kwargs)
		stripe.api_key = settings.STRIPE_SECRET_KEY

		Preference._meta.get_field('storage_price')

		stripe.Plan.create
		self.stripe = stripe






