#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 feed.py
#*====================== #
import os, sys, django
sys.path.append('/sys/centerstack/projects/bs/site')
sys.path.append('/sys/centerstack/projects/bs/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
import requests, sys, bs4, re
from django.core import serializers
from pprint import pprint as pp
import json
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree
from urlparse import urlparse, urljoin
from rets.models import Property
from rets.models import Image


JSON = []
COUNT = 0
offset_range = ["0", "1000"]

for offset in offset_range:
	parser = "lxml"
	username = "CSTACK"
	password = "C3nt3r"
	login_url = "http://rets172lax.raprets.com:6103/CentralOregon/COAR/Login.aspx"
	user_agent = "CenterStack/1.72"
	version = "RETS/1.7.2"
	association = "CentralOregon"
	mls = "COAR"
	base_url = urlparse(login_url).scheme + "://" + urlparse(login_url).netloc
	resource = "Property"
	obj_type = "Photo"


	#	Session
	# ====================================== #
	session = requests.session()
	headers = {'User-Agent':user_agent, 'RETS-Version':version, 'Accept':"*/*"}
	auth = requests.auth.HTTPDigestAuth(username, password)
	session.headers = headers
	session.auth = auth


	#	Login
	#====================================== #
	response_login = session.get(login_url)
	soup = bs4.BeautifulSoup(response_login.text, parser)
	rets_response =  soup.find("rets-response").text.split('\n')
	rets_session_id = session.cookies["RETS-Session-ID"]
	session.headers["RETS-Session-ID"] = rets_session_id
	login_response = {}
	for ii in rets_response:
		if ii.strip():
			key_value_pair = ii.split('=')
			login_response[key_value_pair[0].strip()] = key_value_pair[1].strip()
	session.urls = login_response


	#	Search
	# ====================================== #
	SELECT_LIST = HEADER = ["Acres","Bathrooms","Bedrooms","City","County","Latitude","ListingAgentFullName","ListingDate","ListingPrice","ListingRid","Longitude","MarketingRemarks","MLNumber","PropertyType","Region","RESICOMM","RESIEXTE","RESIHOA","RESIHOAD","RESIHOAP","RESIHTCO","RESIINC1","RESIINC2","RESIINC3","RESIINTE","RESIKITC","RESILEVL","RESIPARK","RESIROOM","RESISTYL","RESIVIEW","RESIWTRD","SquareFootage","State","Status","StatusDate","StreetName","StreetNumber","StreetSuffix","Style","Unit","YearBuilt","ZipCode"]
	SELECT_STR = ','.join(SELECT_LIST)

	if offset == "0":
		params = {
			'Select': SELECT_STR,
			'Format': 'COMPACT-DECODED',
			'Count': '0',
			'Query': "(MLNumber=1+),(Status=|A)",
			'SearchType': "property",
			'QueryType': 'DMQL2',
			'Class': "RESI",
		}
	else:
		params = {
			'Select': SELECT_STR,
			'Format': 'COMPACT-DECODED',
			'Count': '0',
			'Offset': "1001",
			'Query': "(MLNumber=1+),(Status=|A)",
			'SearchType': "property",
			'QueryType': 'DMQL2',
			'Class': "RESI",
		}

	search_url = urljoin(base_url, session.urls['Search'])
	search_response = session.post(search_url, params)
	search_response.raise_for_status()
	soup = bs4.BeautifulSoup(search_response.text, parser)
	search_split =  soup.text.split('\n')


	#	Dynamic Data Structure (Array)
	# ====================================== #
	RETS = {}
	RESULTS = RETS["results"] = []
	for ii in search_split:
		ii = ii.strip()
		ii = ii.split('\t')
		if len(ii) > 1 and ii != SELECT_LIST:
			RESULTS.append(ii)


	#	JSON Construction
	# ====================================== #
	for row in RESULTS:
		k = 0
		JSON_INNER = {}
		for col in SELECT_LIST:
			value = row[k]

			#	Property Image (GetObject)
			# ====================================== #
			if col == "ListingRid":
				photo_url = urljoin(base_url, session.urls["GetObject"])
				photo_response = session.get(photo_url + "?ID=%s:*&Resource=Property&Type=Photo&Location=1" % value)
				photo_response.raise_for_status()
				soup = bs4.BeautifulSoup(photo_response.text, parser)
				links = soup.text.split('\n')

				content_id = 0
				link_dict = {}
				link_array = []
				for link in links:
					link = link.encode('ascii', 'ignore')
					if link.strip() and "simple boundary" not in str(link):
						key = re.split(":(?!\/\/)", link)
						if key[0] == "Content-ID":
							content_id = str(key[1].strip())
						if key[0] == "Location":
							link_array.append(str(key[1].strip()))
				JSON_INNER["img"] = link_array

			JSON_INNER[col] = row[k]
			k+=1

			#	Load each JSON_INNER at different pk
			# ====================================== #
		COUNT += 1
		JSON.append(JSON_INNER)



# ==================================================#
#	Property Model
# ==================================================#
propertyid = 1
imageid = 1
for house in JSON:
	defaults = {}
	for key, value in house.iteritems():
		field = key.lower()
		if field == "img":
			imgs = list(value)
			for img in imgs:
				image_db, created = Image.objects.update_or_create(image_id=str(imageid), defaults={"img":img, "property_id":propertyid})
				image_db.save()
				imageid += 1
		else:
			defaults[field] = value

	property_db, created = Property.objects.update_or_create(property_id=str(propertyid), defaults=defaults)
	property_db.save()
	propertyid += 1















