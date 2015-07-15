import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(';')
    s0=s[0].split(',')
    s1=s[1].split(',')
    print ','.join(sorted(set(s0) & set(s1)))
test_cases.close()