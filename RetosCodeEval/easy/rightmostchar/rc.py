import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(',')[0]
    l=test.strip('\n').split(',')[1]
    i=len(s)-1
    while i > -1:
        if l==s[i]:
            print i
            break
        elif i==0:
            print '-1'
            break
        i=i-1
test_cases.close()