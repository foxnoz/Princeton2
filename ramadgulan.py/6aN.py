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
k = int(sys.argv[2])
i=0
for a in range(1, n+1):
    a2 = a**k
    
    if a2 > n:
        break

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b2 = b**k
        
        if b2 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c2 = c**k
            if c2 > n:
                break

            for d in range(c, n+1):
                d2 = d**k
                if d2 > n:
                    break 

                for e in range(d, n+1):
                    e2 = e**k
                    if e2 > n:
                        break  

                    for f in range(e, n +1):
                        f2 = f**k
                        if f2 > n:
                            break

                        for g in range(1, n+1):
                            g2 = g**k 
                            if g2 > n:
                                break   

                        if a2 + b2 + c2 + d2 + e2 + f2 ==g2:
                            i+=1
                            stdio.write(str(g) + '^'+ str(k) +' = ')
                            stdio.write(str(a) + '^'+str(k) + ' + '+ str(b) + '^'+str(k) +' + ')
                            stdio.write(str(c) + '^'+str(k) +' + '+str(d) + '^'+str(k) +' + ')
                            stdio.write(str(e) + '^' + str(k)+' + '+str(f) + '^' + str(k))
                            stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 