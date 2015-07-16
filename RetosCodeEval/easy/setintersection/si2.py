import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(';')
    s0=s[0].split(',')
    s1=s[1].split(',')
    r=[]
    for i in range(len(s0)):
        if s0[i] in s1:
            r.append(s0[i])
    print ','.join(r)
test_cases.close()