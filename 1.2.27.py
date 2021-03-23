import stdio
import random

# Generate 5 random floats between 0.0 and 1.0. Write them to
# standard output, along with their average value, the min value,
# and the max value.

N = 5

# Generate 5 random floats.
x1 = random.random()
x2 = random.random()
x3 = random.random()
x4 = random.random()
x5 = random.random()

# Write the 5 random floats.
stdio.writeln(x1)
stdio.writeln(x2)
stdio.writeln(x3)
stdio.writeln(x4)
stdio.writeln(x5)

# Compute the stats.
minimum = min(x1, x2, x3, x4, x5)
maximum = max(x1, x2, x3, x4, x5)
average = (x1 + x2 + x3 + x4 + x5) / N

# Write the stats.
stdio.writeln('Average = ' + str(average))
stdio.writeln('Min     = ' + str(minimum))
stdio.writeln('Max     = ' + str(maximum))
