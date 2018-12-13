"""
# The regex version of Double split 
"""
import re

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', line) # 문자의 앞부분에 ^이 있으면 not의 의미이다, * : 0번이상 반복
print(y) 

print('-------------------')
# Even cooler regex version
y = re.findall('^From .*@([^ ]*)', line)
print(y)