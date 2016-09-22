#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	payments/views.py
#*========================== #
from django.shortcuts import render, redirect, HttpResponse
from django.template import RequestContext
from django.conf import settings
import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
	merchant_id=settings.BRAINTREE_MERCHANT_ID,
	public_key=settings.BRAINTREE_PUBLIC_KEY,
	private_key=settings.BRAINTREE_PRIVATE_KEY)
 

@csrf_exempt
def checkout(request):
	rg = request.POST.get
	amount =  request.POST.get('prise') // when user click the subscription for payment
	user = Staff.objects.get(id=request.user.id)
	a_customer_id = ''
	if not user.customer_id:
		result = braintree.Customer.create({
				"first_name": user.first_name,
				"last_name": user.last_name,
				"company": "Braintree",
				"email": user.email,
				"phone": "312.555.1234",
				"fax": "614.555.5678",
				"website": "www.example.com"
		 })
	if result.is_success:
	 user.customer_id = result.customer.id
	 user.save()
	 a_customer_id = user.customer_id
 else:
	a_customer_id = user.customer_id
 if not user.client_token:
	client_token = client_token = braintree.ClientToken.generate({
			 "customer_id": a_customer_id
	 })
	user.client_token = client_token
	user.save()
 else:
	client_token = user.client_token

 varibles ={'amount':amount,'client_token':client_token}
 return render(request, 'checkout.html',varibles)
			…






