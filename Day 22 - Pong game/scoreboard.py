from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.create()

    def create(self):

        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("slow")
        self.goto(x=0, y=240)
        self.display_score()

    def display_score(self):
        self.write(f"{self.score1}:{self.score2}", align=ALIGNMENT, font=FONT)

    def increase_player1_score(self):
        self.score1 += 1
        self.refresh_score()

    def increase_player2_score(self):
        self.score2 += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.display_score()

