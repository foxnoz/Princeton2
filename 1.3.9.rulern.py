#-----------------------------------------------------------------------
# rulern.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer n as a command-line argument. Write to standard
# output the relative lengths of the subdivisions on a ruler of
# order n.

n = int(sys.argv[1])

# Ruler of order 0.
ruler = ' '

# Repeat n times.
for i in range(1, n+1):
    # Concatenate a ruler of order 0, the number i, and a ruler
    # of order 0.
    ruler = ruler + str(i) + ruler

# Write the final result.
stdio.writeln(ruler)

#-----------------------------------------------------------------------

# python rulern.py 0
#  
 
# python rulern.py 1
#  1 
 
# python rulern.py 2
#  1 2 1 
 
# python rulern.py 3
#  1 2 1 3 1 2 1 
 
# python rulern.py 4
#  1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 
 
# python rulern.py 5
#  1 2 1 3 1 2 1 4 1 2 1 3 1 2 1 5 1 2 1 3 1 2 1 4 1 2 1 3 1 2 1

