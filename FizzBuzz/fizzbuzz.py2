__author__ = 'robertb'

import sys

for line in open(sys.argv[1]):
    to_print = []
    line_vars = []
    listNums = line.split(" ")
    for num in listNums:
        line_vars.append(int(num))

    for x in range(1, line_vars[2]+1):
        if x % line_vars[0] == 0 and x % line_vars[1] == 0:
            to_print.append('FB')
            to_print.append(' ')
        elif x % line_vars[0] == 0 and x % line_vars[1] != 0:
            to_print.append('F')
            to_print.append(' ')
        elif x % line_vars[0] != 0 and x % line_vars[1] == 0:
            to_print.append('B')
            to_print.append(' ')
        else:
            to_print.append(str(x))
            to_print.append(' ')

    string = ''.join(to_print)
    print string