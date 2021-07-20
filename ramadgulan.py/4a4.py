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
    a4 = a*a*a*a
    
    if a4 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b4 = b*b*b*b
        
        if b4 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c4 = c*c*c*c
            if c4 > n:
                break

            for d in range(c, n+1):
                d4 = d*d*d*d
                if d4 > n:
                    break 

                for e in range(1, n+1):
                    e4 = e*e*e*e
                    if e4 > n:
                        break       

                    if a4 + b4 + c4 + d4 == e4:
                        i+=1
                        stdio.write(str(e) + '^4 '+' = ')
                        stdio.write(str(a) + '^4 + ' + str(b) + '^4 + ' + str(c) + '^4 + ' + str(d) + '^4')
                        stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 