"""
# Fine-Tuning String Extraction
 - You can refine(개선하다) the match for re.findall() and seperately determine which
   portion of the match is to be extracted by using parentheses(괄호).

# 정규표현식
 - \S : whitespace가 아닌 문자
 - \s : whitespace 문자
 - () : 괄호를 통하여 조건식에는 포함되지만 뽑아내는 부분에서는 제외 할 수 있다
"""

import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x) # \S+ : 공백이 아닌 문자열, @ : 골뱅이, \S+ : 공백이 아닌 문자열
                             # Greedy하게 된다
print(y)

print('-------------------')

# 조건에서 'From '으로 시작하지만 뽑아내는 문자열에는 포함시키고 싶지 않으면 parentheses를 사용한다
y = re.findall('^From (\S+@\S+)', x)
print(y)