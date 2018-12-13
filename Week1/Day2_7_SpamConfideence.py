"""
# Spam confidence
"""
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # 0-9 또는 .으로 시작하여 1개 이상이 반복될 때
    if len(stuff) != 1 : # stuff는 list[]로 반환된다. 따라서 아이템이 이상이 아니면 continue
        continue
    num = float(stuff[0])
    numlist.append(num)
print(numlist)
print('Maximun:', max(numlist));
