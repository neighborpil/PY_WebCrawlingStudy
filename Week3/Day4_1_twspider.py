import urllib.request
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
                (name TEXT,
                 retrieved INTEGER,
                 friends INTEGER)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or type "quit": ') # 가입한 아이디 말고 @아이디를 말한다
    if(acct == 'quit'):
        break;
    if(len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrived Twitter accounts found')
            continue
    
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})

    print('Retriving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining']) # 얼마나 할 수 있는지 보여줌

    js = json.loads(data)
    # Debug
    # print( json.dumps(js, indent=4))

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct,))

    countnew = 0
    countold = 0
    
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))

        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friends))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends) VALUES(?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    
    sqlstr = 'SELECT * FROM Twitter'
    for row in cur.execute(sqlstr):
        print(str(row))

    conn.commit()
   
cur.close()


