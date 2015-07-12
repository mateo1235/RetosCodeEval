import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s = test.strip('\n')
    s = s.split(' ')
    n=s[0]
    l=s[1]
    i=0
    j=0
    sw=True
    while i < len(n) and j < len(l):
        print i
test_cases.close()