import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur =conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
               (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows
               (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or quit: ')
    if(acct == 'quit'): break;

    # 검색 대상의 아이디 가져오기
    if(len(acct) < 1): # 입력한게 없을 때
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try: # retrieved가 0인 아이디가 있으면 하나 가져오고
            (id, acct) = cur.fetchone()
        except: # 없으면 종료
            print('No unretrieved Twitter accounts found')
            continue
    else: # 입력한것이 있을 때
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (acct, ))
        try: # 동일 아이디가 있으면 하나 가져오고
            id = cur.fetchone()[0]
        except: # 없으면 입력
            cur.execute('''INSERT OR IGNORE INTO People
                            (name, retrieved) VALUES (?, 0)''', (acct,))
            conn.commit()
            if cur.rowcount != 1: # 못 집어넣으면 에러
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid
    

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('Retrieving account', acct)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaing', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('Unable to parse json')
        print(data)
        break;

    # Debugging
    # print(json.dumps(js, indent=4))

    if 'users' not in js: # json가져 온거에 users가 없음면 종료
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    # 검색에 사용한 아이디면 retrieved를 1로
    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']: # js에는 users가 많이 있는데 각각의 user들에서
        friend = u['screen_name'] # screen_name을 friend로 하여
        print(friend)
        # People에서 검색하여
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1', (friend,))

        try:
            friend_id = cur.fetchone()[0] 
            countold = countold + 1 # 있으면 countold +1
        except: # 없으면 People에 넣고
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                            VALUES (?, 0)''', (friend,))
            conn.commit()
            if cur.rowcount != 1: # insert error 처리
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid # insert한 People 테이블의 마지막 아이디를 friend_id로
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                        VALUES (?, ?)''', (id, friend_id)) # Follows테이블에 넣는다

    print('New accounts=', countnew, ' revisited=', countold) 
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()

