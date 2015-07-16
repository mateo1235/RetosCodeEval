import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test=int(test.strip('\n'),10)
    if test < 0 or test > 100:
        print 'This program is for humans'
    else:
        if test < 3:
            print 'Still in Mama\'s arms'
        elif test < 5:
            print 'Preschool Maniac'
        elif test < 12:
            print 'Elementary school'
        elif test < 15:
            print 'Middle school'
        elif test < 19:
            print 'High school'
        elif test < 23:
            print 'College'
        elif test < 66:
            print 'Working for the man'
        elif test < 101:
            print 'The Golden Years'
test_cases.close()