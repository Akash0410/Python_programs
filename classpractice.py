from math import pi
from tkinter import X


class area:
    def rectangle(l,b):
        return l*b
    def square(s):
        return s*s
    def circle(r):  
        return pi*(r*r)
    def factorial(f):
        for i in range(1,f+1):
            f=f*i
        return f

print(area.factorial(5))


