import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    p=0
    l=0
    test = test.strip('\n').split(' ')
    for i in range(len(test)):
        if len(test[i]) > l:
            p=i
            l=len(test[i])
    print test[p]
test_cases.close()