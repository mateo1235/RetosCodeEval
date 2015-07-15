import sys
test_cases = open(sys.argv[1], 'r')
m=[[1,2],[2,1],[-1,2],[2,-1],[-2,1],[1,-2],[-1,-2],[-2,-1]]
n2l={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
l2n={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
for test in test_cases:
    pm=[]
    s=list(test.strip('\n'))
    x=l2n[s[0]]
    y=int(s[1],10)
    for i in range(len(m)):
        if m[i][0]+x < 9 and m[i][0]+x > 0 and m[i][1]+y < 9 and m[i][1]+y > 0:
            pm.append(n2l[m[i][0]+x]+str(m[i][1]+y))
    print ' '.join(sorted(pm))
test_cases.close()