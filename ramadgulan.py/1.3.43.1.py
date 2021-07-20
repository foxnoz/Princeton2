import stdio
import sys
    
# Accept integer n as a command-line argument. Write to standard
# output any integer between 1 and n that can be expressed as the
# sum of two cubes in two (or more) different ways.
#
# Bug: If a number can be expressed as a sum of cubes in more than two
# different ways, the program writes some duplicates.

# Accept one command-line argument
n = int(sys.argv[1])


for a in range(1, n+1):
    a2 = a*a
    #stdio.writeln(e2)
    if a2 > n:
        break;

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b2 = b*b
        #stdio.writeln(b2)
        if b2 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c2 = c*c
            #stdio.writeln(str(e2)+' '+str(b2)+' '+str(c2))
            if c2 > n:
                break

            if a2 + b2 == c2:
                stdio.write(str(c) + '^2 '+' = ')
                stdio.write(str(a) + '^2 + ' + str(b) + '^2')
                stdio.writeln()