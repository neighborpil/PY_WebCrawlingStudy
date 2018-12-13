import re
hand = open('test.txt')
for line in hand:
    # print(line)
    line = line.rstrip()
    if re.search('좋아요', line) :
        print(line)

print('-------------------')
hand2 = open('test.txt')

for line in hand2 :
    line = line.rstrip()
    if line.find('좋아요') >= 0:
        print(line)
print('-------------------')
# startwith
hand3 = open('test.txt')
for line in hand3:
    # print(line)
    line = line.rstrip()
    if re.search('^좋아요', line) :
        print(line)

print('-------------------')
hand4 = open('test.txt')

for line in hand4 :
    line = line.rstrip()
    if line.startswith('좋아요'):
        print(line)
        