import stdio
import sys
from time import perf_counter  
# Accept integer n as a command-line argument. Write to standard
# output any integer between 1 and n that can be expressed as the
# sum of two cubes in two (or more) different ways.
#
# Bug: If a number can be expressed as a sum of cubes in more than two
# different ways, the program writes some duplicates.

# Accept one command-line argument
#current = time.localtime(time.time())
t0 = perf_counter()
n = int(sys.argv[1])
i=0
for a in range(1, n+1):
    a2 = a*a
    if a2 > n:
        break;

    for b in range(a, n+1):
        b2 = b*b
        if b2 > n:
            break

        for c in range(b, n+1):
            c2 = c*c
            if c2 > n:
                break

            if a2 + b2 == c2:
                i+=1
                #stdio.write(str(c) + '^2 '+' = ')
                #stdio.write(str(a) + '^2 + ' + str(b) + '^2')
                #stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i))
t1 = perf_counter()
stdio.write('время выполнения = ')
stdio.writeln(t1-t0)
              