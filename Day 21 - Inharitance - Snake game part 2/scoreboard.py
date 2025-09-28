from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()
