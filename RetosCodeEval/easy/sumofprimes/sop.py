i=6
p=[2,3,5]
while len(p)<1000:
    for ii in range(len(p)):
        if i % p[ii] == 0:
            break
        elif ii == len(p)-1:
            p.append(i)
    i=i+1
print sum(p)