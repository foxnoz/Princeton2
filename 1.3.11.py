# digitreverser.py
#-----------------------------------------------------------------------

# Accept an integer command-line argument n. Write to standard
# output the decimal digits of n in reverse order.

import stdio
import sys

n = int(sys.argv[1])

# Reverse using arithmetic.
m = 0
while n != 0:
    m = (10 * m) + (n % 10);
    n //= 10
stdio.writeln(m)

# Just for fun, reverse again using string concatenation.
s = ''
while m != 0:
    digit = m % 10
    s += str(digit)
    m //= 10
stdio.writeln(s)

#-----------------------------------------------------------------------

# python digitreverser.py 12345
# 54321
# 12345
