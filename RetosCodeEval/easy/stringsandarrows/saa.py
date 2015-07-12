import sys
test_cases = open(sys.argv[1], 'r')
l='<--<<'
r='>>-->'
for test in test_cases:
    c = 0
    for i in range(len(test)):
        s = test[i:i+5]
        if l == s or r == s:
            c=c+1
    print c       
test_cases.close()