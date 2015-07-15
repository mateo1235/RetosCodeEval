import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(',')
    i=0
    while i < len(s):
        if s.count(s[i]) > 1:
            s.remove(s[i])
        else:
            i=i+1
    print ','.join(s)
test_cases.close()