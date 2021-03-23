import sys
import stdarray
import stdio

n=int(sys.argv[1])

a=[]
for i in range(n):
	a+=[i]

stdio.writeln (a[n-1])
