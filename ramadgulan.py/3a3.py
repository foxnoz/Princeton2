import stdio
import sys
from time import perf_counter 

t0 = perf_counter()    
n = int(sys.argv[1])
i=0
for a in range(1, n+1):
    a3 = a*a*a
    
    if a3 > n:
        break

    for b in range(a, n+1):
        b3 = b*b*b
        
        if b3 > n:
            break

        for c in range(b, n+1):
            c3 = c*c*c
            if c3 > n:
                break

            for d in range(1, n+1):
                d3 = d*d*d
                if d3 > n:
                    break    

                if a3 + b3 + c3 == d3:
                    i+=1
                    #stdio.write(str(d) + '^3 '+' = ')
                    #stdio.write(str(a) + '^3 + ' + str(b) + '^3 + ' + str(c) + '^3')
                    #stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 
t1 = perf_counter()
stdio.write('время выполнения = ')
stdio.writeln(t1-t0) 