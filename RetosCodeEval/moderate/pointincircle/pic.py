import sys
import math
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip('\n').split(';')
    c=map(float,test[0].split(': ')[1].strip('()').split(', '))
    r=float(test[1].split(': ')[1])
    p=map(float,test[2].split(': ')[1].strip('()').split(', '))
    print str(math.pow(p[0] - c[0], 2) + math.pow(p[1] - c[1],2) < math.pow(r,2)).lower()
test_cases.close()