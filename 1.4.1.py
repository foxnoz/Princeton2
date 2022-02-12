
import stdio
import sys
import stdarray
import random

# Accept integer n as a command-line argument. Write to standard
# output the number of coupons you collect before obtaining one of
# each of n types.

n = int(sys.argv[1])

a = []
for i in range(n):
    value = random.randrange(0, n)
    a += [value]
stdio.writeln(a)
stdio.writeln(a[19])

#------------------------------------