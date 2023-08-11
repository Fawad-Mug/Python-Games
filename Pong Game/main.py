from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


l_paddle= Paddle((-350, 0))
r_paddle= Paddle((350, 0))
ball=Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")


game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect Collision with Wall
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the rightpaddle is mising ball
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()
 
    # Detect when the left paddle is mising ball
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


#1) Create a starting screen
#2) Create and move a paddle
#3) Create a third with OOP Class
#4) Create a ball and move it randomly
#5) Detect Collision with wall and bounce
#6) Detect Collision With Paddle
#7) Detect when pddle is missing
#8) Create a Scoreboard