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
    a4 = a**k
    if a4 > n:
        break;

    # Start at a to avoid print out duplicate.
    for b in range(a, n+1):
        b4 = b**k
        if b4 > n:
            break

        # Start at a + 1 to avoid printing out duplicates.
        for c in range(b, n+1):
            c4 = c**k
            if c4 > n:
                break

            if a4 + b4 == c4:
                i+=1
                stdio.write(str(c) + '^'+str(k) + ' = ')
                stdio.write(str(a) + '^' +str(k)  + ' + '+ str(b) + '^'+str(k))
                stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 