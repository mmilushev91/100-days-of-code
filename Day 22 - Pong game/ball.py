from turtle import Turtle

UP = 90
DOWN = 180

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.create()

    def create(self):
        self.penup()
        self.color("white")
        self.shape("circle")

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(x=new_x, y=new_y)

    def reset(self):
        self.home()
        self.bounce_x()
