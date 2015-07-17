import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=map(int, test.strip('\n').split(' '))
    n=test[0]
    f=test[1::]
    m=100000000
    for i in range(len(f)):
        s=0
        for j in range(len(f)):
            if j!=i:
                s=s+abs(f[i]-f[j])
        if s < m:
            m=s
    print m
test_cases.close()