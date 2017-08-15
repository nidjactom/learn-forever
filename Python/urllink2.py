# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import sys
sys.path.append("C:/Nidhin/learn-forever/Python/Py4e")
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
count = input('Enter count - ')
pos = input('Enter position - ')
loop = 0
while loop <= int(count):
    print('Retrieving:',url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
    tags = soup('a')
    href = tags[int(pos)-1].get('href',None)
    url = href
    loop = loop + 1
