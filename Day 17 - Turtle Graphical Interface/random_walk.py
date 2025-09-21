from turtle import Turtle, Screen
from random import choice

colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "black", "white", "brown", "gray", "cyan", "magenta", "gold",
    "silver", "violet", "indigo", "lime", "turquoise", "navy",
    "maroon", "beige", "tan", "chocolate", "coral", "salmon"
]

headings = [0, 90, 180, 270]

step = Turtle()
step_length = 50
walk_length = 100

#change line width
step.pensize(5)
step.speed("fastest")
#make repetitive
for _ in range(walk_length):
    # set random color
    step.color(choice(colors))
    # set random direction
    step.setheading(choice(headings))
    # move
    step.forward(step_length)

screen = Screen()
screen.exitonclick()
