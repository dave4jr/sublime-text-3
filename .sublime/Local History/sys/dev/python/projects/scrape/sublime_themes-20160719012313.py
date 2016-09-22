# Dave Luke
# Scape colorsublime.com and download all the Sublime Text color themes

import os, sys, codecs
import bs4
from pprint import pprint as pp
import urllib2, urllib
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

print "Theme Scraping Started..."
print ""

pages = 18
save_location = "/Users/Dave/Library/Application Support/Sublime Text 3/Packages/User/color themes"
dl_ext = ".tmTheme"

for ii in range(1,pages+1):

	url = 'http://colorsublime.com/?page=' + str(ii)

	user_agent = {'User-Agent':'Mozilla/5.0'}

	request = urllib2.Request(url,None,user_agent)
	response = urllib2.urlopen(request).read()

	soup = bs4.BeautifulSoup(response)

	sections = soup.find_all('section')

	for section in sections:
		dl_name = str(section.h3.string)
		dl_url = str(section.find('a', class_="btn btn-download").get('href'))
		dl_filename = save_location + '/' + dl_name + dl_ext
		download = urllib.urlretrieve(dl_url,dl_filename)
		print "Download Complete: %s" % dl_name










