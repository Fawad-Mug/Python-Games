import turtle as t
import random 

tim = t.Turtle()
color=["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directios=[1, 90, 180, 270]
tim.speed("fast")
tim.pensize(15)

for _ in range(200):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(directios))