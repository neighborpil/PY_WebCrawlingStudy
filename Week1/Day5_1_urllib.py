import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # encode, get request, make connection
for line in fhand:
    print(line.decode().strip()) # 헤더가 안나옴

print('---------------')
# Open webpage like a file

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words: # 각각의 단어를 돌며
        counts[word] = counts.get(word, 0) + 1 # dictionary에 work, count로 저장
print(counts)

print('---------------')
# Open webpage
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
for line in fhand:
    print(line.decode().strip()) # .strip() : 양쪽 공백을 지운다