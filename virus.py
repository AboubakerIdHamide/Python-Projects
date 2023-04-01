import turtle
#============ !important ====================================
#reset()
#goto(x, y) => move the pen 
#forward(distance)
#backward(distance)
#up() => remove the pen from the screen (stop drawing)
#down() => return the pen 
#left(angle)
#right(angle)
#width(size) => like font-size 
#fill(colorMaybe) => file a close part 
#write("insert text")
#============================================================

# get the app
t= turtle.Turtle()
#get the screen
s=turtle.Screen()
#give the screen bg
s.bgcolor("black")
#speed of pen
t.speed(0)


#give the pen a color
t.pencolor("red")
t.write("Virus")

t.penup()
#replace the pen
t.goto(0,200)
t.pendown()

t.pencolor("green")

a=0
b=0
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==210:
        break
    # hide the pn cursor
    t.hideturtle()

turtle.done()