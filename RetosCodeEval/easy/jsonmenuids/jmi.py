import sys
import json
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n')
    test=json.loads(test)
    s=0
    for i in test['menu']['items']:
        if i != None:
            if len(i)>1:
                s=s+i['id']
    print s
test_cases.close()