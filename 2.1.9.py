import stdio

def duplicate(s):
    t = s + s
    
s = 'Hello'
s = duplicate(s)
t = 'Bye'
t = duplicate(duplicate(duplicate(t)))
stdio.writeln(s + t)
stdio.writeln(s)
