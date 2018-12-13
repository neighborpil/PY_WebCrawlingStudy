"""
# 이메일 주소에서 host만 빼오기
"""
import re
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@') # 문자의 위치
print(atpos)

sppos = data.find(' ', atpos); # 2번째 매개변수는 시작지점
print(sppos)

host = data[atpos+1 : sppos] # @위치 뒤부터 공백까지
print(host)

