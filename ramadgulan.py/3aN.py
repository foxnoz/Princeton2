import stdio
import sys
    
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

            for d in range(1, n+1):
                d2 = d**k
                if d2 > n:
                    break    

                if a2 + b2 + c2 == d2:
                    i+=1
                    stdio.write(str(d) + '^'+ str(k) + ' = ')
                    stdio.write(str(a) + '^'+ str(k) +' + '+ str(b) + '^'+ str(k) +'+' +str(c) + '^2')
                    stdio.writeln()
stdio.writeln('количество комбинаций =' + str(i)) 