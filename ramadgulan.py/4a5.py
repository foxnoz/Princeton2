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

i=0
for a in range(1, n+1):
    a5 = a*a*a*a*a
    
    if a5 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b5 = b*b*b*b*b
        
        if b5 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c5 = c*c*c*c*c
            if c5 > n:
                break

            for d in range(c, n+1):
                d5 = d*d*d*d*d
                if d5 > n:
                    break 

                for e in range(1, n+1):
                    e5 = e*e*e*e*e
                    if e5 > n:
                        break       

                    if a5 + b5 + c5 + d5 == e5:
                        i+=1
                        stdio.write(str(e) + '^5 '+' = ')
                        stdio.write(str(a) + '^5 + ' + str(b) + '^5 + ' + str(c) + '^5 + ' + str(d) + '^5')
                        stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 