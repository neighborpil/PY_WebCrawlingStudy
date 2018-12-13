import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if(len(acct) < 1): break
    url = twurl.augment(TWITTER_URL, {'screen_name': "neighborpil", 'count': '5'}) # screen_name은 트위터에서 @아이디 있는 부분을 말한다

    print('Retriving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    #json.dump(js, indent=4)
    print(js)

    headers = dict(connection.getheaders())
    print('Remainng: ', headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print(' * No status found')
            continue
        s = u['status']['text']
        print('  ', s[:50])

