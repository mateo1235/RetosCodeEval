import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    b=bin(int(test.strip('\n').split(',')[0]))[2:][::-1]
    p=int(test.strip('\n').split(',')[1])
    pp=int(test.strip('\n').split(',')[2])
    print str(b[p-1] == b[pp-1]).lower()
test_cases.close()