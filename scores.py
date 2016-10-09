#!/usr/bin/env python3
n = int((input("Please input the number of students:")))
d = {}
subj = ("math","history","physics")

for i in range(0,n):
    name = input("Please input the name of students:")
    scores = []
    for j in subj:
        scores.append(int(input("Please input the score of %s:" %j)))
    d[name] = scores
for x,y in d.items():
    sc = sum(y)
    print("%s 's total score is %d" %(x,sc))
    if sc > 120:
        print("%s Passed" %x)
    else:
        print("%s Failed" %x)


