import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=int(test.strip('\n'),10)
    print int(test % 2 == 0)
test_cases.close()