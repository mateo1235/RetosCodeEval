import sys
test_cases = open(sys.argv[1], 'r')
s=[' ','\'','*', ':', '.', ',']
for test in test_cases:
    test = list(test.strip('\n'))
    u=True
    for i in range(len(test)):
        if test[i] not in s :
            if u:
                test[i]=test[i].upper()
                u=False
            else:
                test[i]=test[i].lower()
                u=True
    print ''.join(test)
test_cases.close()