import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'drchuck', 'count': '2'})

print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

print('=================')
headers = dict(connection.getheaders())
print(headers)





#TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'

#while True:
#    print('')
#    acct = input('Enter Twitter Account: ')
#    if len(acct) < 1: break;
#    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
#    print('Retrieving', url)
#    connection = urllib.request.urlopen(url)
#    data = connection.read().decode()
#    # print(data)
#    headers = dict(connection.getheaders())
#    print('Remaining', headers['x-rate-limit-remaining'])
#    js = json.loads(data)
#    print(json.dumps(js, indent=4))

#    for u in js['users']:
#        print(u['screen_name'])
        #s = u['status']['text']
        #print('  ', s[:50])