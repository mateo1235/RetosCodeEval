import sys
test_cases = open(sys.argv[1], 'r')
s=0
for test in test_cases:
    test=int(test.strip('\n'),10)
    s=s+test
print s       
test_cases.close()