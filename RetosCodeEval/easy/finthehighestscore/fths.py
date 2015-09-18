import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n')
    test=test.split('|')
    m=[]
    for i in test:
        m.append(i.split(' '))
        while '' in m[len(m)-1]:
            m[len(m)-1].remove('')
        m[len(m)-1]=map(int,m[len(m)-1])
    p=[]
    for i in range(len(m[0])):       
        p.append(max([ j[i] for j in m ]))            
    print ' '.join(map(str,p))
test_cases.close()