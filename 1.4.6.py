import stdarray
import stdio

a= stdarray.create1D(10, 0)
for i in range(10):
	a[i]=9-i

for i in range(10):
    a[i]=a[a[i]]

for v in a:
    stdio.writeln(v)    	