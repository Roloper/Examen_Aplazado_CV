import turtle
from turtle import*

def f(n):
    speed(0)
    if n==0:
        forward(5)
    else:
        f(n-1)
        left(60)
        f(n-1)
        right(120)
        f(n-1)
        left(60)
        f(n-1)
def h(n):
    f(n)
    right(120)
    f(n)
    right(120)
    f(n)

h(4)
turtle.done()