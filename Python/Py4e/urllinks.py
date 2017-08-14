# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://cimpp03.netact.nsn-rdnet.net/mpp/dynamic/logs/version_history?component=product&group=netact&project=netact&version=99.17.07.0.452'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
urlrootsoup = soup('script')
for rootsoup in urlrootsoup:
    print('urlroot =',rootsoup.get('style',None))

##tags = soup('a')
##for tag in tags:
##    if 'LTEA' in tag.get_text():
##        print('Text ->',tag.get_text())
##        print('HREF ->' + url + tag.get('href')[2:])

