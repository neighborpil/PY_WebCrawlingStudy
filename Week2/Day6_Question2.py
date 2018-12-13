"""
[질문 2]http://python-data.dr-chuck.net/comments_42.html 
해당 URL의 html을 load한 후, comments의 총 갯수와 comments에 있는 각 count들을 모두 더해서 출력하는 파이썬 프로그램을 작성해주세요. 
(urllib, BeautifulSoup 등을 import 하여 사용하시면 됩니다.) *
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
html = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(html, 'html.parser')

totalcount = 0
sum = 0

tags = soup('span')
for tag in tags:
    value = tag.getText()
    value = value.strip()
    result = re.findall("[0-9]+", value)
    if len(result) == 1:
        totalcount += 1
        sum += int(value)
print('totalcount: ', totalcount)
print('sum: ', sum)