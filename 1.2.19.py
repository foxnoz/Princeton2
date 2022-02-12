import stdio
import math
import sys
G=9.80665
x = float(sys.argv[1])
v= float(sys.argv[2])
t = float(sys.argv[3])
a=x+v*t-G*t**2/2
stdio.writeln(a)
