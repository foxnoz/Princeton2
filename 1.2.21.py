import stdio
import math
import sys

t = float(sys.argv[1])
P= float(sys.argv[2])
r = float(sys.argv[3])
a=P*math.exp(r*t)
stdio.writeln(a)