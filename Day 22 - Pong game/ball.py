from turtle import Turtle

UP = 90
DOWN = 180

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.create()
    
  def create(self):
    self.penup()
    self.color("white")
    self.shape("circle")
    
  def move(self):
    # new_x = self.xcor() + 10 if self.xcor() > 0 else self.xcor() - 10
    # new_y = 0
    
    # if self.ycor() > 300:
    #   self.setheading(180)
    #   new_y = self.ycor() + 10
      
    # elif self.ycor() < -300:
    #   self.setheading(90)
    #   new_y = self.ycor() - 10

    new_x = self.xcor() + 10 
    new_y = self.ycor() + 10
      
    
    self.goto(x=new_x, y=new_y)


    
