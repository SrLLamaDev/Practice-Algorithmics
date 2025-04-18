# This program draws a simple landscape with mountains, a sun, and trees using the turtle graphics library.
# It uses functions to create different shapes and colors for the elements in the scene.
# The turtle moves to specific coordinates to draw each part of the landscape.
# The turtle is hidden at the end of the drawing.
# The background color is set to sky blue, and the grass is drawn in lime green.
import turtle
from turtle import *
speed(0)
bgcolor("skyblue")


penup()
goto(-400, -100)
pendown()
color("limegreen")
begin_fill()
for i in range(2):
    forward(800)
    right(90)
    forward(400)
    right(90)
end_fill()

penup()
goto(-400, -100)
pendown()
color("dimgray")
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

penup()
goto(100, -100)
pendown()
begin_fill()
for i in range(3):
    forward(300)
    left(120)
end_fill()

penup()
goto(-160, -100)
pendown()
color("gray")
begin_fill()
for i in range(3):
    forward(400)
    left(120)
end_fill()

penup()
goto(-35, 120)
pendown()
color("white")
begin_fill()
left(35)
forward(60)
right(90)
forward(30)
left(100)
forward(45)
right(85)
forward(65)
left(160)
forward(150)
end_fill()

penup()
goto(-215, 100)
pendown()
color("snow")
begin_fill()
forward(70)
left(120)
forward(75)
left(150)
forward(45)
right(90)
forward(45)
left(120)
end_fill()

penup()
goto(203, 80)
pendown()
begin_fill()
forward(95)
right(120)
forward(80)
right(150)
forward(50)
left(70)
end_fill()

left(50)

penup()
goto(-500, 350)
pendown()
color("yellow")
begin_fill()
circle(125)
end_fill()

def tree():
    color("saddlebrown")
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
    
    forward(10)
    left(90)
    forward(5)
    
    color("forestgreen")
    begin_fill()
    circle(25)
    end_fill()
    
    right(90)

penup()
goto(-25,-200)
pendown()
tree()
    
penup()
goto(200,-150)
pendown()
tree()

penup()
goto(300,-250)
pendown()
tree()

penup()
goto(-300,-250)
pendown()
tree()

penup()
goto(-200,-100)
pendown()
tree()

hideturtle()