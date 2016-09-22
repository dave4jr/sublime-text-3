#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	interface/views.py
#*========================== #
import requests, socket, hashlib, urllib, time, os, sys, logging, bs4, re
from pprint import pprint as pp
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree
from urlparse import urlparse, urljoin
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import ContactForm
# from .forms import SellForm
# from .models import Rets


parser = "lxml"
username = "CSTACK"
password = "C3nt3r"
login_url = "http://rets172lax.raprets.com:6103/CentralOregon/COAR/Login.aspx"
user_agent = "CenterStack/1.72"
version = "RETS/1.7.2"
association = "CentralOregon"
mls = "COAR"
base_url = urlparse(login_url).scheme + "://" + urlparse(login_url).netloc




# #	Contact
# # ====================================== #
# def contact(request, template):
# 	if request.method == "POST":
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			messages.success(request, "We will get back to you as soon as possible. Thank you!")
# 	else:
# 		form = ContactForm()
# 	return render(request, template, {"ContactForm": form })



# #	Sell
# # ====================================== #
# def sell(request, template):
# 	if request.method == "POST":
# 		form = SellForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form = SellForm()
# 	return render(request, template, {"SellForm": form })



#	RETS
# ====================================== #
def login():
	session = requests.session()
	headers = {'User-Agent':user_agent, 'RETS-Version':version, 'Accept':"*/*"}
	auth = requests.auth.HTTPDigestAuth(username, password)
	session.headers = headers
	session.auth = auth


	#	Login Response / Convert To Dictionary
	# ====================================== #
	response_login = session.get(login_url)
	soup = bs4.BeautifulSoup(response_login.text, parser)
	rets_response =  soup.find("rets-response").text.split('\n')
	login_response = {}
	for ii in rets_response:
		if ii.strip():
			key_value_pair = ii.split('=')
			login_response[key_value_pair[0].strip()] = key_value_pair[1].strip()
	session.urls = login_response
	return session



#	Metadata
# ====================================== #
def get_metadata(request, template):
	session = login()
	meta_url = urljoin(base_url, session.urls["GetMetadata"])
	response = session.get(meta_url + '?Type=METADATA-SYSTEM&ID=*')
	session.metadata = response
	print session.metadata
	return session



#	Search
# ====================================== #
def search():
	session = login()
	params = {
		'Select': "ListingRid",
		'Format': 'COMPACT-DECODED',
		'Count': '0',
		'Query': "(MLNumber=1+),(Status=|A)",
		'SearchType': "property",
		'QueryType': 'DMQL2',
		'Class': "RESI",
	}
	search_url = urljoin(base_url, session.urls['Search'])
	search_response = session.post(search_url, params)
	search_response.raise_for_status()

	soup = bs4.BeautifulSoup(search_response.text, parser)
	session.search = soup.text
	print session.search
	return session.search



# select = "ListingRid,MLNumber,Status,City,LastModifiedDateTime"
# query = "(MLNumber=1+),(Status=|A)"
# search(select, query, search_type, search_class)



#	Get Object
# ====================================== #
def get_object(obj_id, resource, obj_type):
	session = login()
	go_url = urljoin(base_url, session.urls["GetObject"])
	go_response = session.get(go_url + "?ID=%s:*&Resource=%s&Type=%s&Location=1" % (obj_id, resource, obj_type))
	go_response.raise_for_status()

	soup = bs4.BeautifulSoup(go_response.text, parser)
	links = soup.text.split('\n')

	content_id = 0
	link_dict = {}
	link_array = []
	for link in links:
		if link.strip() and "simple boundary" not in str(link):
			key = re.split(":(?!\/\/)", link)
			if key[0] == "Content-ID":
				content_id = str(key[1].strip())
			if key[0] == "Location":
				link_array.append(str(key[1].strip()))

	link_dict[content_id] = link_array
	# pp(link_dict["179886"][1])


# obj_id = "179886"
# resource = "Property"
# obj_type = "Photo"
# get_object(obj_id, resource, obj_type)



#	Main
# ====================================== #
def main(request, template):
	search()
	logging.debug(search)
	logging.debug("hello")
	print "hello"

	sell_form = SellForm()
	contact_form = ContactForm()
	context = {
		"ContactForm": sell_form,
		"SellForm": contact_form,
		"search": search,
	}
	return render(request, template, context)











