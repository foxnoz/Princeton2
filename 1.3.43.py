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
    #stdio.writeln(str('a5')+'='+str(a5))
    if a5 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(1, n+1):
        b5 = b*b*b*b*b
        #stdio.writeln(str('b5')+'='+str(b5))
        if b5 > n:
            break;

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(1, n+1):
            c5 = c*c*c*c*c
            #stdio.writeln(str('c5')+'='+str(c5))
            if c5 > n:
                break

            # Start at c to avoid printing out duplicates.
            for d in range(1, n+1):
                d5 = d*d*d*d*d
                #stdio.writeln(str('d5')+'='+str(d5))
                if d5 > n:
                    break

                for e in range(1, n+1):
            	     e5 = e*e*e*e*e
            	     #stdio.writeln(str('e5')+'='+str(e5))
            	     if e5 > n:
            	         break
                    
                if c5 + d5 + a5 + b5 == e5:
                    stdio.write(str(a5+b5+c5+d5) + ' = ')
                    stdio.write(str(e5))
                    #stdio.write(str(c) + '^4 + ' + str(d) + '^4')
                    stdio.writeln()

#-----------------------------------------------------------------------

# python ramanujanfor.py 2000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3

# python ramanujanfor.py 10000
# 1729 = 1^3 + 12^3 = 9^3 + 10^3
# 4104 = 2^3 + 16^3 = 9^3 + 15^3

