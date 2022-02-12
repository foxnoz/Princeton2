import stdio
import sys

n = int(sys.argv[1])

total = 0
for i in range(2, 11):
    digit = n % 10;   # крайняя правая цифра
    total += i * digit
    n //= 10
    stdio.writeln(digit)
    stdio.writeln(n)