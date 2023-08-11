from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1

    def move(self):
        new_x=  self.xcor() + self.x_move
        new_y=  self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        """This function return bal bounce if it collide with y-axis or -y-axis"""
        """if ball is go up we move dwon or vice versia so we multilply it with negative number to move in oppsoite direction return back"""
        self.y_move *= -1

    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.bounce_x()