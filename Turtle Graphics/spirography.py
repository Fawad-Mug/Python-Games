import turtle as t
import random 

tim = t.Turtle()
tim.speed("fastest")

t.colormode(255)
def c_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color = (r, g, b)
    return color

def draw_spiralgrapgh(size_of_gap):
    for _ in range(int(360 / size_of_gap)) :
        tim.color(c_color())
        tim.circle(100)
        tim.setheading(tim.heading()+ size_of_gap)

draw_spiralgrapgh(5)

screen=t.Screen()
screen.exitonclick()