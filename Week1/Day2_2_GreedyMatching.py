"""
# Greedy matching
 - 매칭하는 것이 여러개 있을 때에 가장 긴 것을 선택한다
  - The repeat character (+ and *) push outward in both directions
    (greedy) to match the largest possible string.

# .
 - 모든 문자에 대응한다
 - a.b : a + 모든문자 + b

"""
# Greedy matching
import re
x = 'From: Using the : charcter'
y = re.findall('^F.+:', x) # ^F : F로 시작하는 문자열, .+ : 모든 문자열을 추가한다, ':' : :로 끝이난다
                           # 'From:'도 될 수 있고, 'From: Using the :'도 될 수 있다. 둘 중 긴거 선택
print(y)

print('-------------------')


# Non-greedy matching
y = re.findall('^F.+?:', x) # ?의 의미는 문자열을 추가하는데 not greedy하게, 짧은거 선택
print(y)