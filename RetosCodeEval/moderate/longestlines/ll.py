import sys
test_cases = open(sys.argv[1], 'r')
d=[]
i=0
n = test_cases.readline().strip('\n')
for test in test_cases:
    s = test.strip('\n')
    d.append(s)
d.sort(lambda x,y: cmp(len(x), len(y)), reverse=True)
while i < int(n,10):
    print d[i]
    i=i+1
test_cases.close()