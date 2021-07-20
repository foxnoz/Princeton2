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
    a6 = a*a*a*a*a*a
    
    if a6 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b6 = b*b*b*b*b*b
        
        if b6 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c6 = c*c*c*c*c*c
            if c6 > n:
                break

            for d in range(c, n+1):
                d6 = d*d*d*d*d*d
                if d6 > n:
                    break 

                for e in range(d, n+1):
                    e6 = e*e*e*e*e*e
                    if e6 > n:
                        break  

                    for f in range(1, n +1):
                        f6 = f*f*f*f*f*f
                        if f6 > n:
                            break

                        if a6 + b6 + c6 + d6 + e6 == f6:
                            i+=1
                            stdio.write(str(f) + '^6 '+' = ')
                            stdio.write(str(a) + '^6 + ' + str(b) + '^6 + ' + str(c) + '^6 + ' + str(d) + '^6 +' + str(e) + '^6')
                            stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i))                             