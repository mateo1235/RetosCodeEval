p=[2]
pp=[]
i=3
while i < 1000:
    for ii in range(len(p)):
        if i % p[ii] == 0:
            break
        elif ii == len(p)-1:
            p.append(i)
            if str(i) == str(i)[::-1]:
                pp.append(i)
    i=i+1
print pp[-1]