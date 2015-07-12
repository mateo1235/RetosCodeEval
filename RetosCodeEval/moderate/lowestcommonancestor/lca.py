import sys
test_cases = open(sys.argv[1], 'r')
d={'10':[20,8,30,10],'29':[20,8,30,29],'20':[8,30,20],'3':[8,30,3],'8':[30,8],'52':[30,52],'30':[30]}
for test in test_cases:
    r = False
    ns = test.strip('\n').split(' ')
    a=ns[0]
    b=ns[1]
    if a in d.keys() and b in d.keys():
        la=d[a]
        lb=d[b]     
        for i in range(len(la)):
            for j in range(len(lb)):
                if la[i] == lb[j]:
                    print la[i]
                    r = True
                    break        
            if r:
                break
test_cases.close()