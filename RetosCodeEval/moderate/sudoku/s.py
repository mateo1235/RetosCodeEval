import sys
def valid(l):
    vistos = set()
    unicos = []
    for x in l:
        if x not in vistos:
            unicos.append(x)
            vistos.add(x)
    return len(unicos) == len(l)
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n').split(';')
    n=int(test[0],10)
    s=test[1].split(',')
    s=[s[i:i+n] for i in range(0, len(s), n)]
    c=[s[j][0:n] for j in range(0, len(s), 1)]
    v=True
    for j in range(len(s)):
        if not valid(s[j]):
            v=False            
            break
    print v            
test_cases.close()