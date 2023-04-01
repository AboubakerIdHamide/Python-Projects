import turtle

from pyparsing import col 
t= turtle.Turtle()
s= turtle.Screen()
t.hideturtle()
s.bgcolor("black")
t.speed(0)
t.pencolor("white")
def cool(longeur):
    x=365/5
    for j in range(int(x)):
    #=== careé =======
        for i in range(4):
            t.forward(longeur)
            t.left(90)
    # ================
        t.left(5)
   
cool(200)


turtle.done()