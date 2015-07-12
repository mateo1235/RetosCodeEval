import sys
import math
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    c = 0
    n = int(test.strip('\n'),10)
    while n != 1 and c < 100:        
        n = sum(map(int, [(math.pow(int(list(str(n))[i],10),2)) for i in range(len(list(str(n))))]))
        c=c+1
    print int(n == 1)        
test_cases.close()