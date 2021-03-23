import stdio

# Read integers from standard input until end-of-file. Then write
# the maxmimum an minimum of the integers to standard output.

maximum = stdio.readInt()
minimum = maximum

while not stdio.isEmpty():
    value = stdio.readInt()
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value

    stdio.writeln('maximum = ' + str(maximum) + \
                  ', minimum = ' + str(minimum))
