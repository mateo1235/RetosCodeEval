import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    u=0.0
    l=0.0
    s=test.strip('\n')
    for i in range(len(s)):
        if s[i].islower():
            l=l+1.0
        elif s[i].isupper():            
            u=u+1.0
    t=u+l
    rl="%.2f" % round((l/t)*100,2)
    ru="%.2f" % round((u/t)*100,2)
    print "lowercase: "+str(rl)+" uppercase: "+str(ru)
test_cases.close()