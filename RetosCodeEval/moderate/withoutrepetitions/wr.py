import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = list(test.strip('\n'))
    i=0  
    while i < len(test)-1:
        if test[i]==test[i+1]:
            test.pop(i+1)
        else:
            i=i+1
    print ''.join(test)
test_cases.close()