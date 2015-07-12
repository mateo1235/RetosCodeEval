import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(' ')
    l = 0
    p = 0
    for i in range(len(test)):
        if len(test[i]) > l:
            l = len(test[i])
            p = i
    s = test[p]
    r=''
    for j in range(len(s)):
        r=r+("*"*j)+s[j]+" " 
    print r[:-1]
test_cases.close()