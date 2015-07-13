import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=[]
    i=0
    test = test.strip('\n')
    while i < len(test):
        try:
            if test[i] == '(' or test[i] == '{' or test[i] == '[':
                s.append(test[i])
            elif test[i] == ')' and s[len(s)-1]=='(':
                s.pop()
            elif test[i] == '}' and s[len(s)-1]=='{':
                s.pop()
            elif test[i] == ']' and s[len(s)-1]=='[':
                s.pop()
            else:
                break
        except IndexError:
            break
        i=i+1        
    print len(s) == 0
test_cases.close()