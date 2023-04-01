import turtle
from turtle import *

t= Turtle()
t.speed(0)
t.hideturtle()
def square():
    for i in range(4):
        t.forward(20)
        t.left(90)
t.goto(-75,0)
y=0
for i in range(8):
    if i%2==0:
        for j in range(8):
            if j%2==0:
                t.begin_fill()
                t.fillcolor("black")
                square()
                t.end_fill()
            else:
                square()
            t.forward(20)
    else:
        for j in range(8):
            if j%2!=0:
                t.begin_fill()
                t.fillcolor("black")
                square()
                t.end_fill()
            else:
                square()
            t.forward(20)


    y+=20
    t.penup()
    t.goto(-75,y)
    t.pendown()

t.penup()
t.goto(0, y+40)
t.pendown()
t.write("yeah bro Done!", align="center", font= 40)


turtle.done()



