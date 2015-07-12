for i in range(1,13):
    print ''.join([str(j*i)+' '*(5-(len(str(j*i)))) for j in range(1,13)])