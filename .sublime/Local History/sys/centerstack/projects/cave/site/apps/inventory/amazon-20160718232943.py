#*======================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Client:		CMA
#*  Description:	inventory/views.py
#*======================== #
import os, sys, django, requests, re, json, logging, bs4
sys.path.append('/sys/centerstack/projects/cave/site')
sys.path.append('/sys/centerstack/projects/cave/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
from django.shortcuts import render, redirect
from django.conf import settings
from xml.etree import ElementTree
from urlparse import urlparse, urljoin
from inventory.models import Inventory
from inventory.forms import InventoryForm
import amazonproduct


#	Config
# ========================= #
# config = {
# 	'access_key': "AKIAIV7UBXGWGXBNGXOQ",
# 	'secret_key': "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",
# 	'associate_tag': "dave4jr-20",
# 	'locale': "us"
# }
# api = amazonproduct.API(cfg=config)
# items = api.item_lookup("079400379979", SearchIndex='All', IdType='UPC')

# for item in items:
# 	try:
# 		print item
# 	except:
# 		pass

# http://webservices.amazon.com/onca/xml?
#   Service=AWSECommerceService
#   &Operation=ItemLookup
#   &ResponseGroup=Large
#   &SearchIndex=All
#   &IdType=UPC
#   &ItemId=635753490879
#   &AWSAccessKeyId=[Your_AWSAccessKeyID]
#   &AssociateTag=[Your_AssociateTag]
#   &Timestamp=[YYYY-MM-DDThh:mm:ssZ]
#   &Signature=[Request_Signature]

#*====================== #
#*  Author:    Dave Luke Jr
#*  Company:   CenterStack.io
#*  Description:   feed.py
#*====================== #
import os, sys, django, requests, bs4, re, json
sys.path.append('/sys/centerstack/projects/cave/site')
sys.path.append('/sys/centerstack/projects/cave/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
import datetime
from django_cron import CronJobBase, Schedule
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree
from urlparse import urlparse, urljoin


class InventoryData():

  def __init__(self):
    self.parser = "lxml"
    self.service = "AWSECommerceService"
    self.operation = "ItemLookup"
    self.response_group = "Large"
    self.search_index = "All"
    self.access_key = "AKIAIV7UBXGWGXBNGXOQ"
    self.secret_key = "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"
    self.associate_tag = "dave4jr-20"
    self.locale = "us"
    self.timestamp = datetime.datetime.now()


  def search(self, item_id, id_type):
    url = "http://webservices.amazon.com/onca/xml?Service=%s&Operation=%s&ResponseGroup=%s&SearchIndex=%s&IdType=%s&ItemId=%s&AWSAccessKeyId=%s&AssociateTag=%s&Timestamp=%s&Signature=[Request_Signature]"
    (self.service, self.operation, self.response_group, self.search_index, id_type, item_id, self.access_key, self.associate_tag, self.timestamp)
  
a = InventoryData()





# # Session
# # ====================================== #
# session = requests.session()
# headers = {'User-Agent':user_agent, 'RETS-Version':version, 'Accept':"*/*"}
# auth = requests.auth.HTTPDigestAuth(username, password)
# session.headers = headers
# session.auth = auth


# # Login
# #====================================== #
# response_login = session.get(login_url)
# soup = bs4.BeautifulSoup(response_login.text, parser)
# rets_response =  soup.find("rets-response").text.split('\n')
# rets_session_id = session.cookies["RETS-Session-ID"]
# session.headers["RETS-Session-ID"] = rets_session_id
# login_response = {}
# for ii in rets_response:
#   if ii.strip():
#     key_value_pair = ii.split('=')
#     login_response[key_value_pair[0].strip()] = key_value_pair[1].strip()
# session.urls = login_response


# # Search
# # ====================================== #
# SELECT_LIST = HEADER = ["Acres","Bathrooms","Bedrooms","City","County","Latitude","ListingAgentFullName","ListingDate","ListingPrice","ListingRid","Longitude","MarketingRemarks","MLNumber","PropertyType","PropertySubtype1","PropertySubtype2","PropertySubtype3","RESICOMM","RESIEXTE","RESIHOA","RESIHOAD","RESIHOAP","RESIHTCO","RESIINC1","RESIINC2","RESIINC3","RESIINTE","RESIKITC","RESILEVL","RESIPARK","RESIROOM","RESISTYL","RESIVIEW","RESIWTRD","SquareFootage","State","Status","StatusDate","StreetName","StreetNumber","StreetSuffix","Style","Unit","YearBuilt","ZipCode"]
# SELECT_STR = ','.join(SELECT_LIST)
# params = {
#   'Select': SELECT_STR,
#   'Format': 'COMPACT-DECODED',
#   'Count': '0',
#   'Offset': offset,
#   'Query': "(MLNumber=1+),(Status=|A)",
#   'SearchType': "property",
#   'QueryType': 'DMQL2',
#   'Class': "RESI",
# }

# search_url = urljoin(base_url, session.urls['Search'])
# search_response = session.post(search_url, params)
# search_response.raise_for_status()
# soup = bs4.BeautifulSoup(search_response.text, parser)
# search_split =  soup.text.split('\n')


    








