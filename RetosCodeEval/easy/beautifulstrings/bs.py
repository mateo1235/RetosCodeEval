#!/usr/bin/python
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=0
    l=[]
    test=test.strip().lower()
    while len(test)>0:
        if test[0].islower():
            l.append(test.count(test[0]))
        test=test.replace(test[0].lower(),'')            
    l=sorted(l,reverse=True)
    m=26
    for k in range(len(l)):
        s=s+l[k]*m
        m=m-1
    print s
test_cases.close()