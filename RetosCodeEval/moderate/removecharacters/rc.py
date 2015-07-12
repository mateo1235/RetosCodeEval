import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    p = test.strip('\n').split(', ')[0]
    r = test.strip('\n').split(', ')[1]
    for i in range(len(r)):
        while r[i] in p:
            p=p.replace(r[i],"")
    print p
test_cases.close()