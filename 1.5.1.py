#-----------------------------------------------------------------------
# addints.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer command-line argument n. Read n integers from the
# standard input stream, and write their sum to standard output.

n = int(sys.argv[1])

total = 0
for i in range(n):
    total += stdio.readInt()

stdio.writeln('Sum is ' + str(total))

#-----------------------------------------------------------------------

# python addints.py 5   
# 18 19 20 21 22
# Sum is 100


