from turtle import Turtle, Screen
import random


is_race_on= False
screen = Screen()
screen.setup(width=500, height=400)
user_guess= screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")

colors=["red", "orange", "green", "yellow", "blue", "purple"]
y_directions=[-70, -40, -10, 20, 50, 80]
all_turtle=[]


for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230 , y=y_directions[i])
    all_turtle.append(new_turtle)


if user_guess:
    is_race_on = True

while is_race_on:


    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color== user_guess:
                print(f"You've won!. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost!. The {winning_color} turtle is the winner!")
        random_distance= random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
