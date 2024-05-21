import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
# cp = ["red","blue","yellow"]
# cp2 = random.choice(cp)
a =0
b = 0
t.speed(-1)
t.penup()
t.goto(0,200)
t.pendown()
while  True:
    cp = ["red","blue","yellow","pink","green","purple","orange"]
    cp2 = random.choice(cp)
    t.pencolor(cp2)
    t.pensize(4)
    t.forward(a)
    t.right(b)
    a+=5
    b+=1
    if b ==210:
        break
    t.hideturtle()

turtle.done()