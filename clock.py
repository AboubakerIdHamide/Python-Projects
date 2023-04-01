import turtle
import time

from numpy import angle

t= turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0,-100)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(100)
t.end_fill()
t.penup()
t.goto(0,-60)
t.pendown()
t.begin_fill()
t.fillcolor("#ffffff")
t.circle(60)
t.end_fill()
# write numbers
t.penup()
t.home()
t.left(90)
for n in range(12):
    t.right(360/12)    
    t.forward(85)     # comme diamétre
    t.write(n+1)
    t.goto(0,0)       # retour au centre

def arm_hour():
    t.penup()
    t.home()
    t.right(180)
    t.pendown()
    t.pensize(5)
    t.forward(40)

def arm_min():
    t.penup()
    t.home()
    t.right(270)
    t.pendown()
    t.pensize(3)
    t.forward(70)


arm_hour()
arm_min()

angel1=0
while True:
    start_time=time.time()
    f_start=1
    if f_start==1:
        t.penup()
        t.home()
        t.pensize(2)
        t.left(70)
        f_start=2
    t.right(angel1)
    t.pendown()
    t.forward(60)
    time.sleep(1-(time.time() - start_time))
    t.undo()#remove the line
    t.goto(0,0)
    t.right(360/60)
    angel1+=360/60
    

turtle.done()