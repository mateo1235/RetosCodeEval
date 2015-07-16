import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' : ')
    s=test[0].split(' ')
    p=test[1].split(', ')
    for i in range(len(p)):
        p1=int(p[i].split('-')[0],10)
        p2=int(p[i].split('-')[1],10)
        a=s[p1]
        s[p1]=s[p2]
        s[p2]=a
    print ' '.join(s)
test_cases.close()