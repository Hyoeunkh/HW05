#!/usr/bin/python
import sys

text = str(sys.argv[1])
num = int(sys.argv[2])

file = open(text, 'r')
line = file.readline()

word = line.split()

dic = {}

for w in word:
        if w not in dic:
                dic[w] = dic.get(w,1)
        else:
                dic[w] += 1
list = list(dic.keys())
key = sorted(dic.values(), reverse=True)


for x in range(20):
        print("%s%10d" % (list[x],key[x]))

file.close()
