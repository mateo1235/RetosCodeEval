import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' ')
    a=int(test[0],10)
    b=int(test[1],10)
    c=int(test[2],10)
    n=1
    r=''
    while n <= c:
        if  n % a == 0 and n % b == 0:
            r=r+"FB "
        elif  n % a == 0:
            r=r+"F "
        elif  n % b == 0:
            r=r+"B "
        else:
            r=r+str(n)+" "
        n=n+1
    print r[:-1]
test_cases.close()