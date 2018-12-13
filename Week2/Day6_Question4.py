"""
[질문 4] http://python-data.dr-chuck.net/comments_353540.json
해당 URL의 json을 load한 후, comments의 총 갯수와 comments에 있는 각 count들을 모두 더해서 출력하는 파이썬 프로그램을 작성해주세요.
(urllib, json 등을 import 하여 사용하시면 됩니다.) *
"""
import urllib.request, urllib.parse, urllib.error
import json
import re
try:
    data = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_353540.json').read().decode()
    js = json.loads(data)
except:
   js = None
if not js:
    print('==== Failure To Retrieve ====')
    print(js)
else:
    totalcount = 0
    sum = 0;
    for line in js["comments"]:
        value = line['count']
        totalcount += 1
        sum += value
    print('totalcount: ', totalcount)
    print('sum: ', sum)


