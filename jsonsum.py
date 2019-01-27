import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print("count",len(info['comments']))

tot = 0
for item in info['comments']:
    nbr = item['count']
    num = int(nbr)
    tot += num
print("Sum:", tot)
