import stdio
import sys
from time import perf_counter 
t0 = perf_counter()
n = int(sys.argv[1])
i=0
for a in range(1, n+1):
    a4 = a*a*a*a
    if a4 > n:
        break;

    for b in range(a, n+1):
        b4 = b*b*b*b
        if b4 > n:
            break

        for c in range(b, n+1):
            c4 = c*c*c*c
            if c4 > n:
                break

            if a4 + b4 == c4:
                i+=1
                #stdio.write(str(c) + '^4 '+' = ')
                #stdio.write(str(a) + '^4 + ' + str(b) + '^4')
                #stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 
t1 = perf_counter()
stdio.write('время выполнения = ')
stdio.writeln(t1-t0)                