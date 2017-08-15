import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = input('Enter location: ')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
sum = 0
cnt = 0
for item in info['comments']:
    sum = sum + int(item['count'])
    cnt = cnt + 1
print('Count:',cnt)
print('Sum:',sum)