#-----------------------------------------------------------------------
# fiveperline.py
#-----------------------------------------------------------------------

import stdio

# Write to standard output the integers from 1000 (inclusive) to 2000
# (exclusive), 5 integers per line.

START = 1000
END = 2000
INTS_PER_LINE = 5

for i in range(START, END):
    stdio.write(str(i) + ' ')
    if i % INTS_PER_LINE == INTS_PER_LINE-1:
        stdio.writeln()
stdio.writeln()

