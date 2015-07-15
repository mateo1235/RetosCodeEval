import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=test.strip('\n').split(' | ')
    s0=map(int,s[0].split(' '))
    s1=map(int,s[1].split(' '))
    r=[]
    for i in range(len(s0)):
        r.append(s0[i]*s1[i])
    print ' '.join(map(str,r))
test_cases.close()