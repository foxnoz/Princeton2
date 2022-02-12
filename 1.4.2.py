import stdio
import stdarray
from math import sqrt
 
def dist_1(x,y): # способ 1
    d=0
    for i in range(len(x)):
        d+=(x[i]-y[i])**2
    return sqrt(d)
    
def dist_2(x,y): # способ 2
    return sqrt(sum(map(lambda p: (p[0]-p[1])**2,zip(x,y))))
    
stdio.writeln(dist_1((1,2,3),(3,2,1)))    
stdio.writeln(dist_2((1,2,3),(3,2,1)))