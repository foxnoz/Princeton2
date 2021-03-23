import stdio
import random
import sys

# Generate 5 random floats between 0.0 and 1.0. Write them to
# standard output, along with their average value, the min value,
# and the max value.

n = int(sys.argv[1])

# Generate n random floats.
a=0
for x in range (n):
	a+=1
	x = random.random()
	stdio.writeln (a)
	stdio.writeln (x)
	                 
	
# Write the 5 random floats.
#stdio.writeln(x1)


# Compute the stats.
minimum = min (x)
#maximum = max(x1, x2, x3, x4, x5)
#average = (x1 + x2 + x3 + x4 + x5) / N

# Write the stats.
#stdio.writeln('Average = ' + str(average))
stdio.writeln('Min     = ' + str(minimum))
#stdio.writeln('Max     = ' + str(maximum))
#не решил
