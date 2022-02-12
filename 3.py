import stdarray
import sys
import stdio

n= int(sys.argv[1])
perm = stdarray.create1D(n, 0)
for i in range(n):
	perm[i]=i
    stdio.write(str(perm))
    #не работает	