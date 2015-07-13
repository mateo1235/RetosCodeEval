import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    i=0
    test = test.strip('\n').split(' | ')
    ns=map(int,test[0].split(' '))
    while i < int(test[1],10):
        for i in range(len(ns)-1):
            if ns[i]>ns[i+1]:
                a = ns[i+1]
                ns[i+1]=ns[i]
                ns[i]=a     
        i=i+1
    print ' '.join(map(str, (ns[0:])))
test_cases.close()