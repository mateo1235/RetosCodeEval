import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' ')
    r=[]
    for i in range(len(test)):
        r.append(test[i][0].upper()+test[i][1::])
    print ' '.join(r)
test_cases.close()