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
 

#	Main View
# ========================= #
def main(request, template):
	context = {}
	return render(request, template, context)





