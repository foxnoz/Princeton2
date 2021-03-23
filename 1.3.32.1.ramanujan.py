#-----------------------------------------------------------------------
# ramanujanfor.py
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
for a in range(1, n+1):
    a3 = a*a*a
    if a3 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b3 = b*b*b
        if a3 + b3 > n:
            break;

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(a+1, n+1):
            c3 = c*c*c
            if c3 > a3 + b3:
                break

            # Start at c to avoid printing out duplicates.
            for d in range(c, n+1):
                d3 = d*d*d
                if c3 + d3 > a3 + b3:
                    break

                if c3 + d3 == a3 + b3:
                    stdio.write(str(a3+b3) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()

#-----------------------------------------------------------------------

# python ramanujanfor.py 2000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

# python ramanujanfor.py 10000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3
# 4104 = 2^3 + 16^3 = 9^3 + 15^3

