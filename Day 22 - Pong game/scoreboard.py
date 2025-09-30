from turtle import Turtle 

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.create()
    
  def create(self):
    self.score1 = 0
    self.score2 = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.speed("slow")
    self.goto(x=0, y=240)
    self.display_score()

  def display_score(self):
    self.write(f"{self.score1}:{self.score2}", align=ALIGNMENT, font=FONT)
