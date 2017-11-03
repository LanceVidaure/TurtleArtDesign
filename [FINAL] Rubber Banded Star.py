import turtle #first section - setups
lance = turtle.Turtle()
from StarFunctionFile import*
lance.width(3)
turtle.bgcolor("black")
from random import*
turtle.colormode(255)

lance.pencolor("brown") #second section - making a brown spiral
spiral = 1
lance.pendown()
lance.speed(0)
for times in range (200):
   lance.forward(spiral)
   lance.left(90)
   spiral = spiral+10   

lance.pencolor("blue") #third section - making a blue rectangle
lance.speed(11)
x3 = -820
y3 = -475
teleport(lance,x3,y3)
lance.pendown()
lance.speed(5)
for times in range(2):
    lance.forward(1640)
    lance.left(90)
    lance.forward(960)
    lance.left(90)

lance.speed(11) #fourth section - making a blue jail cell
x4 = -820
y4 = 475
teleport(lance,x4,y4)
for times in range(47):
    lance.pendown()
    lance.forward(1640)
    lance.right(90)
    lance.forward(10)
    lance.right(90)
    lance.forward(1640)
    lance.left(90)
    lance.forward(10)
    lance.left(90)
lance.forward(1640)

lance.pencolor("green") #fifth section - making a green circle
x = 0
y = -475
lance.speed(100)
teleport(lance,x,y)
lance.speed(3)
lance.circle(475)

x1 = 0 #sixth section - making a rubber banded-like star
y1 = 0
lance.speed(11)
teleport(lance,x1,y1)
for times in range(84):
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    c = (r,g,b)
    lance.forward(times*10)
    lance.right(144)
    rubberbandedstar(lance,250,c)

lance.hideturtle() #seventh section - have fun! :)  
turtle.done()
