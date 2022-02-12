# digitreverser.py
#-----------------------------------------------------------------------

# Accept an integer command-line argument n. Write to standard
# output the decimal digits of n in reverse order.

import stdio
import sys
f=0
g=1
for i in range(16):
    stdio.writeln(f)
    f=f+g
    g=f-g

#-----------------------------------------------------------------------

# python digitreverser.py 12345
# 54321
# 12345
