import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' ')
    r=''
    for i in range(0, len(test), 2):
        if test[i]=='00':
            r=r+'1'*len(test[i+1])
        elif test[i]=='0':
            r=r+test[i+1]
    print int(r,2)
test_cases.close()