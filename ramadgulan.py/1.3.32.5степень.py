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

# For each a, b, c, d, check whether a^4 + b^4 = c^4 + d^4.
for a in range(1, n+1):
    a5 = a*a*a*a*a
    if a5 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b5 = b*b*b*b*b
        if a5 + b5 > n:
            break;

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(a+1, n+1):
            c5 = c*c*c*c*c
            if c5 > a5 + b5:
                break

            # Start at c to avoid printing out duplicates.
            for d in range(c, n+1):
                d5 = d*d*d*d*d
                if c5 + d5 > a5 + b5:
                    break

                if c5 + d5 == a5 + b5:
                    stdio.write(str(a5+b5) + ' = ')
                    stdio.write(str(a) + '^5 + ' + str(b) + '^5 = ')
                    stdio.write(str(c) + '^5 + ' + str(d) + '^5')
                    stdio.writeln()

#-----------------------------------------------------------------------

# python ramanujanfor.py 2000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

# python ramanujanfor.py 10000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3
# 4104 = 2^3 + 16^3 = 9^3 + 15^3
