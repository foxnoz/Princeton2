import sys
import stdio
n=int(sys.argv[1])
for a in range(1, n+1):
	stdio.write(str(a)+ '=' + int(a))
	for b in range(a, n+1):
		stdio.write(b)
		for c in range(a+1, n+1):
			stdio.write(c)
			for d in range(c, n+1):
				stdio.write(d)
				