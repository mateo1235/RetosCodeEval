#r=100%
import sys
test_cases = open(sys.argv[1], 'r')
d={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0','':' '}
for test in test_cases:
    test=test.strip('\n')
    l=test.split(" ")
    s=""
    for i in l:
        s=s+d[i]
    print s
test_cases.close()