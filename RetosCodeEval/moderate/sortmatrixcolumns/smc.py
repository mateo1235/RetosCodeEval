import sys
def compare(m):
    i=0
    while i < len(m)-1:         
        for j in range(len(m[i])):
            if m[i][j]>m[i+1][j]:
                a=m[i]
                m[i]=m[i+1]
                m[i+1]=a
                break
        i=i+1
    return m
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' | ')
    m=[test[i].split(' ') for i in range(len(test))]
    if len(test)>0:
        m = compare(m)
        print ' |'.join(m)            
test_cases.close()