import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    r=''
    s=sorted(map(float, list(test.strip('\n').split(' '))))
    for i in range(len(s)):
        r=r+ "%.3f" % round(s[i], 3)+' '
    print r
test_cases.close()