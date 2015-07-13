import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip('\n').split('| ')
    ls=list(test[0])
    ns=test[1].split(' ')
    r=''
    for i in range(len(ns)):
        r=r+ls[int(ns[i],10)-1]
    print r
test_cases.close()