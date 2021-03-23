import stdio
import sys

# Accept integers representing a month (m), day (d), and year (y) as
# command-line arguments. Write to standard output the day of the week
# of the date m/d/y according to the Gregorian calendar. For m use 1
# for January, 2 for February, and so forth. For the day of the week
# use 0 for Sunday, 1 for Monday, and so forth.

m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0//400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0)//12) % 7

stdio.writeln(d0)

#-----------------------------------------------------------------------

# python day.py 8 2 1953
# 0
