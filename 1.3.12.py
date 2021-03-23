#-----------------------------------------------------------------------
# fibonacci.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer n as a command-line argument. Write to standard
# output the first n Fibonacci numbers.

n = int(sys.argv[1])

f = 0
g = 1

for i in range(0, n):
    f = f + g
    g = f - g
    stdio.writeln(f)
    stdio.writeln(g)
