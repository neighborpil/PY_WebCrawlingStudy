"""
# Web scraping
 - When a program or script pretends to be a browser and retrives web pages, looks at those web pages,
   extracts information, and then looks at more web pages

 - Search engines scraping web pages - we call this "spidering the web' or "web crawling"
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') # html을 파싱하고, 수정

# Retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) # 만약 href의 대상이 되는 것이 있다면 출력