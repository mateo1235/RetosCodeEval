import sys
import math
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').strip(')').strip('(').split(' ')
    p1=int(test[0].strip(')').strip('(').split(',')[0],10)
    p2=int(test[1].strip(')').strip('(').split(',')[0],10)
    p3=int(test[2].strip(')').strip('(').split(',')[0],10)
    p4=int(test[3].strip(')').strip('(').split(',')[0],10)
    print int(math.sqrt(math.pow(p3-p1, 2)+math.pow(p4-p2, 2)))
test_cases.close()