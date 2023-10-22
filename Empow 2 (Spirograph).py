from turtle import *

def fan():
    i=0
    while i < 3:
        for fan in range(240):
            forward(fan/2+30)
            backward(fan/2+30)
            right(0.5)
        if i < 4:
            i += 1

        
fan()
