import sys
test_cases = open(sys.argv[1], 'r')
l="<--<<"
r=">>-->"
for test in test_cases:
    c = 0
    for i in range(len(test)):
        if l == test[i:i+5] or r == test[i:i+5]:
            c=c+1
    print c       
test_cases.close()