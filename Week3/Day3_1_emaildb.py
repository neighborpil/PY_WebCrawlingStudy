"""
SQL Light Browser 깔고 확인 및 테스트
"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute("""
Drop TABLE IF EXISTS Counts""")
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if(len(fname) < 1): 
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): # 이메일 서두만 따기
        continue
    pieces = line.split()
    email = pieces[1] # From 이후 이메일 주소만 따기
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # email로 select 해서
    row = cur.fetchone() # 값을 가져오는데 
    if row is None: # 없으면 insert
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    else: # 있으면 update count 
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' # 마지막 10개만 가져오기
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()