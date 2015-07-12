import sys
d={'1':'I','5':'V','10':'X','50':'L','100':'C','500':'D','1000':'M'}
dd=[1,5,10,50,100,500,1000]
ddd=['I','V','X','L','C','D','M']
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    o=[]
    i=0
    n=int(test,10)
    while n>0:
        num=dd[len(dd)-i-1]
        r=n/num
        if r > 0:
            o.append(d[str(num)]*r)
            n=n%num
            i=i+1
        else:
            i=i+1

    for ii in range(len(o)):
        lim = ddd.index(o[ii-1][0])+1
        limm = ddd.index(o[ii][0])+1        
        if len(list(o[ii]))>3:
            if len(ddd)>lim or len(ddd)>limm :
                if (o[ii-1][0] == 'V' or o[ii-1][0] == 'L' or o[ii-1][0] == 'D'):
                    a=(o[ii])[0]
                    o[ii]=ddd[lim]
                    o[ii-1]=a
                else:
                    o[ii]=(o[ii])[0]+ddd[limm] 
    print ''.join(o)
test_cases.close()