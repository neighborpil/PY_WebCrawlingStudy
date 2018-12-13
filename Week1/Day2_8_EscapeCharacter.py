"""
# Escape character
 - 사용하다 보면 특수한 regular expression의 실제 문자를 사용하고 싶을 때에는
 - 앞에다가 '\'를 붙여주면 된다
 - special character가 아니라 그냥 문자가 된다
"""

import re
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x) # \$ : real dollar sign
print(y)
