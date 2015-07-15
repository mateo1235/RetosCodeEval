import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n')
    print int(s,16)
test_cases.close()