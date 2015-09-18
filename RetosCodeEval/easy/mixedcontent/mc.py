#r=100%
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n')
    l=test.split(",")
    n=[]
    p=[]
    for i in l:
        try:
            e = int(i,10)
            n.append(i)
        except Exception as inst:
            p.append(i)
    if len(n)>0 and len(p) > 0:
        print ','.join(p)+"|"+','.join(n)
    elif len(n)>0:
        print ','.join(n)
    elif len(p)>0:
        print ','.join(p)
test_cases.close()