from turtle import *
import turtle

t= Turtle()
s= Screen()
s.bgcolor("black")
t.pencolor("white")
t.hideturtle()
t.width(2)

#=== careé =======
for i in range(4):
    t.forward(100)
    t.left(90)
# ================

t.left(30)
t.forward(60)
t.right(30)
t.forward(100)
t.right(150)
t.forward(60)
t.right(120)
t.forward(100)
t.right(60)
t.forward(60)
t.left(150)

#=== careé =======
for i in range(4):
    t.forward(100)
    t.left(90)
# ================

t.forward(100)
t.left(30)
t.forward(60)

    


turtle.done()