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
    a3 = a*a*a
    
    if a3 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b3 = b*b*b
        
        if b3 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c3 = c*c*c
            if c3 > n:
                break

            for d in range(c, n+1):
                d3 = d*d*d
                if d3 > n:
                    break 

                for e in range(d, n+1):
                    e3 = e*e*e
                    if e3 > n:
                        break  

                    for f in range(1, n +1):
                        f3 = f*f*f
                        if f3 > n:
                            break

                        if a3 + b3 + c3 + d3 + e3 == f3:
                            i+=1
                            stdio.write(str(f) + '^3 '+' = ')
                            stdio.write(str(a) + '^3 + ' + str(b) + '^3 + ' + str(c) + '^3 + ' + str(d) + '^3 +' + str(e) + '^3')
                            stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 