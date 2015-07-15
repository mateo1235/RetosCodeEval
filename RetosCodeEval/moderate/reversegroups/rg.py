import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    r=''
    n = int(test.strip('\n').split(';')[1],10)
    test = test.strip('\n').split(';')[0].split(',')
    test=[test[i:i+n] for i in range(0, len(test), n)]
    for i in range(len(test)):
        if len(test[i]) % n == 0:
            r=r+','.join((test[i][::-1]))+','
        else:
            r=r+','.join(test[i])+','
    print r[:-1]
test_cases.close()