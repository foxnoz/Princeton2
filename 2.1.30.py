# benford.py
#-----------------------------------------------------------------------

import stdio
import stdarray

#-----------------------------------------------------------------------

# Верните начальную цифру x, предполагая, что x-положительное целое число.

def leadingDigit(x):
    while x >= 10:
        x //= 10
    return x

#-----------------------------------------------------------------------

# Считайте последовательность целых чисел из стандартного ввода, вычисляйте и
# запись в стандартный вывод частотного распределения числа
# раз 1-9 является ведущей (левой) цифре.

# Закон Бенфорда предсказывает, что для многих реальных наборов данных:
#
#   digit  frequency
#   ----------------
#       1       30.1
#       2       17.6
#       3       12.5
#       4        9.7
#       5        7.9
#       6        6.7
#       7        5.8
#       8        5.1
#       9        4.6

counts = stdarray.create1D(10, 0)  # frequency of leading digit i
n = 0                              # number of items read in

while not stdio.isEmpty():
    x = stdio.readInt()       # read in next integer
    digit = leadingDigit(x)   # compute leading digit
    counts[digit] += 1        # update frequency
    n += 1

# Write the frequency distribution.
for i in range(1, len(counts)):
    stdio.writef("%d: %6.1f%%\n", i, 100.0 * float(counts[i]) / float(n))
    
#-----------------------------------------------------------------------

# python benford.py < princeton-files.txt 
# 1:   30.8%
# 2:   19.3%
# 3:   13.0%
# 4:    9.9%
# 5:    7.4%
# 6:    5.9%
# 7:    5.2%
# 8:    4.4%
# 9:    4.1%