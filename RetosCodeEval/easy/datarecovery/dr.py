import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(';')
    l=test[0].split(' ')
    n=test[1].split(' ')
    r=['' for i in range(len(l))]
    i=0
    while len(l) > 1:
        r[int(n[i],10)-1]=l[0]
        l[0]=''
        l.remove('')
        i=i+1
    r[r.index('')]=l[0]
    sorted(r)
    print ' '.join(r)
test_cases.close()