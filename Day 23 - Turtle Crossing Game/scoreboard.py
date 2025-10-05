from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-250, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create()

    def create(self):
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.display_level()

    def display_level(self):
        self.write(arg=f"LEVEL: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)
