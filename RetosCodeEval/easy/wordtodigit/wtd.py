import sys
test_cases = open(sys.argv[1], 'r')
d={'zero':'0', 'one':'1','two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
for test in test_cases:
    r=''
    test = test.strip('\n').split(';')
    for i in range(len(test)):
        r=r+d[test[i]]
    print r
test_cases.close()