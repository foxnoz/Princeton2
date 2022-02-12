#-----------------------------------------------------------------------
# transpose.py
#-----------------------------------------------------------------------

import stdio
import sys
import stdarray

# Принять целочисленный аргумент командной строки n. Создайте массив n на n и
# запишите его в стандартный вывод. Затем перенесите его на место и напишите
# результат на стандартный вывод.

# Оригинальная версия Java от Кристиана Рубио.

# Создайте массив нулей n на n.
n = int(sys.argv[1])
a = stdarray.create2D(n, n, 0)

# Populate the array.
# Заполнить массив.
for r in range(n):
    for c in range(n):
        a[r][c] =  n*r + c
        
# Write the initial array.
stdio.writeln("Before")
stdio.writeln("------")
for row in a:
    for element in row:
        stdio.write('%4d' % element)
    stdio.writeln()

# Transpose the array in-place.
for r in range(n):
    for c in range(r+1, n):
        temp = a[r][c]
        a[r][c] = a[c][r]
        a[c][r] = temp

# Write the transposed array.
stdio.writeln()
stdio.writeln("After")
stdio.writeln("------")
for row in a:
    for element in row:
        stdio.write('%4d' % element)
    stdio.writeln()
    
#-----------------------------------------------------------------------

# python transpose.py 0
# Before
# ------
# 
# After
# ------
# 

# python transpose.py 1
# Before
# ------
#    0
# 
# After
# ------
#    0

# python transpose.py 2
# Before
# ------
#    0   1
#    2   3
# 
# After
# ------
#    0   2
#    1   3

# python transpose.py 3
# Before
# ------
#    0   1   2
#    3   4   5
#    6   7   8

# After
# ------
#    0   3   6
#    1   4   7
#    2   5   8

# python transpose.py 4
# Before
# ------
#    0   1   2   3
#    4   5   6   7
#    8   9  10  11
#   12  13  14  15

# After
# ------
#    0   4   8  12
#    1   5   9  13
#    2   6  10  14
#    3   7  11  15

# python transpose.py 5
# Before
# ------
#    0   1   2   3   4
#    5   6   7   8   9
#   10  11  12  13  14
#   15  16  17  18  19
#   20  21  22  23  24

# After
# ------
#    0   5  10  15  20
#    1   6  11  16  21
#    2   7  12  17  22
#    3   8  13  18  23
#    4   9  14  19  24

