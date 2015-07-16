import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    l=10
    p=0
    test=map(int,test.strip('\n').split(' '))
    for i in range(len(test)):
        if test.count(test[i]) == 1 and test[i] < l:
            l=test[i]
            p=i+1
    print p
test_cases.close()