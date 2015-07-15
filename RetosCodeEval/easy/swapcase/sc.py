import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    s=list(test.strip('\n'))
    for i in range(len(s)):
        if s[i].islower():
            s[i]=s[i].upper()
        elif s[i].isupper():
            s[i]=s[i].lower()
    print ''.join(s)
test_cases.close()