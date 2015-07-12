#!/usr/bin/python
i=0
n=3992
nn='3992'
d={'1':'I','5':'V','10':'X','50':'L','100':'C','500':'D','1000':'M'}
dd=[1,5,10,50,100,500,1000]
ddd=['I','V','X','L','C','D','M']
o=[]

while n>0:
    num=dd[len(dd)-i-1]
    r=n/num
    if r > 0:
        o.append(d[str(num)]*r)
        n=n%num
    else:
        i=i+1
        r=1

for i in range(len(o)):
    if len(list(o[i]))>3:
        a=(o[i])[0]
        o[i]=ddd[ddd.index(o[i-1][0])+1]
        o[i-1]=a
print o
        

    