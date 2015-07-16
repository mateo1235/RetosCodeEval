import sys
test_cases = open(sys.argv[1], 'r')
b=[[0 for x in range(256)] for x in range(256)] 
for test in test_cases:
    test=test.strip('\n').split(' ')
    o=test[0]
    i=int(test[1],10)
    if o == 'SetRow':
        x=int(test[2],10)
        for j in range(len(b[i])):
            b[i][j]=x
    elif o == 'SetCol':
        x=int(test[2],10)
        for j in range(len(b[i])):
            b[j][i]=x
    elif o == 'QueryRow':
        s=0
        for k in range(len(b[i])):
            s=s+b[i][k]
        print s
    elif o == 'QueryCol':
        s=0
        for l in range(len(b[i])):
            s=s+b[l][i]
        print s  
test_cases.close()