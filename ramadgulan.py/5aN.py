import stdio
import sys
from time import perf_counter  

t0 = perf_counter()
n = int(sys.argv[1])
k = int(sys.argv[2])
i=0
for a in range(1, n+1):
    a2 = a**k
    
    if a2 > n:
        break

    for b in range(a, n+1):
        b2 = b**k
        
        if b2 > n:
            break

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

                    for f in range(1, n +1):
                        f2 = f**k
                        if f2 > n:
                            break

                        if a2 + b2 + c2 + d2 + e2 == f2:
                            i+=1
                            #stdio.write(str(f) + '^'+ str(k) +' = ')
                            #stdio.write(str(a) + '^'+str(k) + ' + '+ str(b) + '^'+str(k) +' + ')
                            #stdio.write(str(c) + '^'+str(k) +' + '+str(d) + '^'+str(k) +' + '+str(e) + '^' + str(k))
                            #stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i))
t1 = perf_counter()
stdio.write('время выполнения = ')
stdio.writeln(t1-t0)