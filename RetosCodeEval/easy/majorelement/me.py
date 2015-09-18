#r=0% CodeEval Error: Process was aborted after 10 seconds
import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=test.strip('\n')
    test=test.split(',')
    i=0
    while True:
        if i >= len(test):
            print("NONE")
            break
        if test.count(test[i]) > len(test)/2:
            print(test[i])
            break
        i=i+1
test_cases.close()