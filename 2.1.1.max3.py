import stdio
import sys
def max3(a, b, c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return(max)
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3]) 
result=max3   
stdio.writeln(result)

