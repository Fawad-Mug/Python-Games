import turtle as t
import random 

color=["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

dog= t.Turtle()

def draw(sides):
    angle= 360/ sides
    for _ in range (sides):
        dog.forward(100)
        dog.right(angle)


for i in range(3,11):
    dog.color(random.choice(color))
    draw(i)
