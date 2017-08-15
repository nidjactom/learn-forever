import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum = sum + int(count.text)
print('count:', len(counts))
print('sum:', sum)