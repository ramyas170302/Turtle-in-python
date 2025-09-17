import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.setup(800,800)
s.title("basic math geometry")
t.penup()
#draw circle
t.goto(-100,100)
t.pendown()
t.color("red","yellow")
t.begin_fill()

t.circle(50)
t.end_fill()
t.penup()
# draw square
t.goto(100,100)

t.color("blue","orange")
t.begin_fill()
t.pendown()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
# to draw triangle
t.penup()
t.goto(-100,-100)
t.color("violet","lime")
t.begin_fill()

t.pendown()
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120)
t.end_fill()
# to draw pentagonal
t.penup()
t.goto(100,-100)
t.color("magenta","cyan")
t.begin_fill()
t.pendown()
for i in range(5):
    t.forward(100)
    t.left(360/5)
t.end_fill()
# to draw hexagonal
t.penup()
t.goto(0,-300)
t.color("purple","pink")
t.begin_fill()
t.pendown()

for i in range(6):
    t.forward(100)
    t.left(360/6)
t.end_fill()

turtle.done()
