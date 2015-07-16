import sys
import datetime
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pass
    #===========================================================================
    # test=test.strip('\n').split(' ')
    # t1='{dt:%A}'.format(test[0])
    # t2='{dt.hour}/{dt.minute}/{dt.second}'.format(test[1])
    # f = '%H:%M:%S'
    # if datetime.strptime(test[0], f) > datetime.strptime(test[1], f):
    #     print datetime.strptime(test[0], f) - datetime.strptime(test[1], f)
    # else:
    #     print (datetime.strptime(test[1], f) - datetime.strptime(test[0], f)).strftime('%m/%d/%Y %I:%M%p')
    #===========================================================================
test_cases.close()