#r=100%
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    a=''
    test=test.strip('\n')
    test=test.split(' ')
    i=1
    b=[]
    b.append(test[0])
    while True:
        if i == len(test):
            a=a+str(len(b))+" "+b[0]
            break
        if b[0]==test[i]:
            b.append(test[i])
        else:
            a=a+str(len(b))+" "+b[0]+" "
            b = []
            b.append(test[i])
        i=i+1        
    print a
test_cases.close()