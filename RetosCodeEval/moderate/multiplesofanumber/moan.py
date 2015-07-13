import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip('\n').split(',')
    x=int(test[0],10)
    n=int(test[1],10)
    m=0
    while m < x:
        m=m+n
    print m
test_cases.close()