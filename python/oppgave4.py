import turtle

s = turtle.getscreen()
t = turtle.Turtle()

turtle.title("My Turtle Program")


t.shapesize(3,2,1)
t.color("green", "green")

for i in range(12):
    for x in range(6):
     t.begin_fill()
     t.fd(100)
     t.rt(60)
    t.rt(30)

input()