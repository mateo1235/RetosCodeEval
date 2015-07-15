import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(' ')
    print s[-2]
test_cases.close()