import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    i=0
    test = test.strip('\n').split(',')
    n=int(test[0],10)
    m=int(test[1],10)
    while n >= m:
        n=n-m      
    print n
test_cases.close()