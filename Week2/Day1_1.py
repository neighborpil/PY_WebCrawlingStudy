"""
# ASCII code
 - 0 to 256 represents characters and numbers which is storen in 1 byte

# ord()
 - The ord() function tells us the numeric value of a ASCII character 

 # Multi-byte chracters
 - UTF-16 : 2bytes, fixed length
 - UTF-32 : 4bytes, fixed length
 - UTF-8 : 1-4 bytes
"""

print(ord('H'))
print(ord('e'))
print(ord('\n'))
# python3이상에서는
x = b'abc' # byte는 따로 관리된다
print(type(x))
x = '이광춘'
print(type(x)) # string과 unicode가 같다
x = u'이광춘'
print(type(x))

# 네트워크를 통하여 데이터를 수신할 경우 데이터에 맞도록 decoding을 해주어야 한다
"""
example: 
while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)
"""