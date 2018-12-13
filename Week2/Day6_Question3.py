"""
[질문 3] http://python-data.dr-chuck.net/comments_42.xml
해당 URL의 xml을 load한 후, comments의 총 갯수와 comments에 있는 각 count들을 모두 더해서 출력하는 파이썬 프로그램을 작성해주세요. 
(urllib, xml.etree.ElementTree 등을 import 하여 사용하시면 됩니다.) *
"""
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import re

raw = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.xml').read()
lines = raw.decode()

stuff = ET.fromstring(lines)
lst = stuff.findall('comments/comment')
sum = 0;

for item in lst:
    word = item.find('count').text
    word = word.strip()
    check = re.findall("[0-9]+", word)
    if len(check) == 1:
        sum += int(check[0])

print('totalcount: ', len(lst))
print('sum: ', sum)