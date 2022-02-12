import sys
import stdio
n = int (sys.argv[1])
total = О
for i in range( n ) :
    total+= stdio.readInt( )
stdio.writeln('Sum is' + str(total))