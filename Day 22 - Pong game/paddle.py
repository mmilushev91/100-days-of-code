from turtle import Turtle

START_Y = 0
PACE = 20
UP_ANGLE = 90
DOWN_ANGLE = 270
UP_LIMIT = 280
DOWN_LIMIT = -280


class Paddle(Turtle):

    def __init__(self, start_x):
        super().__init__()
        self.start_x = start_x
        self.create()

    def create(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(UP_ANGLE)
        self.penup()
        self.goto(x=self.start_x, y=START_Y)
        self.color("white")

    def up(self):
        if self.ycor() + PACE < UP_LIMIT:
            self.forward(PACE)

    def down(self):
        if self.ycor() - PACE > DOWN_LIMIT:
            self.backward(PACE)
