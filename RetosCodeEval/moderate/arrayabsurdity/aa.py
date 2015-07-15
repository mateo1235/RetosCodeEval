import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(';')
    if len(test)>0:
        n=test[0]
        s=test[1].split(',')
        vistos = set()
        for x in s:
            if x not in vistos:                
                vistos.add(x)
            else:
                print x
                break                
test_cases.close()