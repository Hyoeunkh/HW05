#!/usr/bin/python
import sys
import re
text = str(sys.argv[1])
num = int(sys.argv[2])

file = open(text, 'r')
line = re.sub("[.,!?]", "", file.readline())
word = line.split()

dic = {}

for w in word:
        if w not in dic:
                dic[w] = dic.get(w,1)
        else:
                dic[w] += 1

sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for x in range(num):
        print("%-15s%5d" % (sort[x][0], sort[x][1]))

file.close()


