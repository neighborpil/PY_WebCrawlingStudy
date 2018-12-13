"""
# re.search()
 - 조건에 맞는지 true/false를 반환한다

# re.findall()
 - 조건에 맞는 string의 리스트를 반환한다

# 반복
 - * : 0번 반복도 허용
       ca*t : ct, cat, caat
 - + : 1번 이상부터 반복 혀용
       ca+t : cat, caat, caaat
"""
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x); # [0-9] : 한자리 이상의 숫자, + : 1회 이상
print(y)

print('-------------------')

y = re.findall('[AEIOU]+', x)
print(y)

print('-------------------')

y = re.findall('[aeiou]+', x)
print(y)