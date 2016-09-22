#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 feed.py
#*====================== #
import os, sys, django, requests, bs4, re, json
sys.path.append('/sys/centerstack/projects/cave/site')
sys.path.append('/sys/centerstack/projects/cave/site/apps')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
django.setup()
from django.db.models import Count
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree
from urlparse import urlparse, urljoin


parser = "lxml"
username = "CSTACK"
password = "C3nt3r"
login_url = "https://api.bookeo.com/v2"
user_agent = "CenterStack/1.72"
version = "RETS/1.7.2"
association = "CentralOregon"
mls = "COAR"
base_url = urlparse(login_url).scheme + "://" + urlparse(login_url).netloc
resource = "Property"
obj_type = "Photo"

















