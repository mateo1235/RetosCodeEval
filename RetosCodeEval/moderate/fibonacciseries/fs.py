import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=int(test.strip('\n'),10)
    a=0
    aa=1
    i=0
    while i <test:
        x=a
        a=a+aa
        aa=x
        i=i+1  
    print a          
test_cases.close()