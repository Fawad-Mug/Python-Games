import turtle as t
import random 

tim = t.Turtle()
directios=[1, 90, 180, 270]
tim.speed("fast")
tim.pensize(15)

t.colormode(255)
def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range(200):
    tim.color(color())
    tim.forward(30)
    tim.setheading(random.choice(directios))