import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    i=3
    p=[2]
    test = map(int, test.strip('\n').split(','))
    n=0
    while i <= test[1]:
        for ii in range(len(p)):
            if i % p[ii] == 0:
                break
            elif ii == len(p)-1:
                p.append(i)                
                if i > test[0]:
                    n=n+1
        i=i+1
    if test[0] == 2:
        print n+1
    else:
        print n
test_cases.close()