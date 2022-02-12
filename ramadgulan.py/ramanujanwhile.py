#-----------------------------------------------------------------------
# ramanujanwhile.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept integer n as a command-line argument. Write to standard
# output any integer between 1 and n that can be expressed as the
# sum of two cubes in two (or more) different ways.
#
# Bug: If a number can be expressed as a sum of cubes in more than two
# different ways, the program writes some duplicates.

# Accept one command-line argument.
n = int(sys.argv[1])

# For each a, b, c, d, check whether a^3 + b^3 = c^3 + d^3.
a = 1
while a <= n:
    a3 = a*a*a
    if a3 > n:
        break

    # Start at a to avoid print out duplicate.
    b = a
    while b <= n:
        b3 = b*b*b
        if a3 + b3 > n:
            break;

        # Start at a + 1 to avoid printing out duplicates.
        c = a+1
        while c <= n:
            c3 = c*c*c
            if c3 > a3 + b3:
                break

            # Start at c to avoid printing out duplicates.
            d = c
            while d <= n:
                d3 = d*d*d
                if c3 + d3 > a3 + b3:
                    break

                if c3 + d3 == a3 + b3:
                    stdio.write(str(a3+b3) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()
                d += 1
            c += 1
        b += 1
    a += 1
    
#-----------------------------------------------------------------------

# python ramanujanwhile.py 2000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

# python ramanujanwhile.py
# 100001729 = 1^3 + 12^3 = 9^3 + 10^3
# 4104 = 2^3 + 16^3 = 9^3 + 15^3
