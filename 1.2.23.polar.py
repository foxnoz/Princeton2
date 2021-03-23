# polar.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# Accept floats x and y as command-line arguments. Convert Cartesian
# coordinates (x, y) to polar coordinates (r, theta), and write r and
# theta to standard output.

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x*x + y*y)
theta = math.atan2(y, x)

stdio.writeln('r     = ' + str(r))
stdio.writeln('theta = ' + str(theta))

