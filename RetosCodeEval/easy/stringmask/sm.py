import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' ')
    l=list(test[0])
    n=test[1]
    for i in range(len(l)):
        if n[i] == '1':
            l[i]=l[i].upper()
    print ''.join(l)
test_cases.close()