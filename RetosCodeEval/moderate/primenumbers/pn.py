import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    i=6
    p=[2,3,5]
    test = int(test.strip('\n'),10)
    while i < test:
        for ii in range(len(p)):
            if i % p[ii] == 0:
                break
            elif ii == len(p)-1:
                p.append(i)
        i=i+1
    print ','.join(map(str, p))
test_cases.close()