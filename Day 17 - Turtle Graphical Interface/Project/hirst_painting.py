import turtle
import colorgram
from turtle import Turtle, Screen
from random import choice

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

screen = Screen()
turtle.colormode(255)
painter = Turtle()
painter.penup()
painter.speed("fastest") 
painter.hideturtle()

for y in range(-220, 280, 50):
    for x in range(-220, 280, 50):
        painter.goto(x, y)
        painter.dot(20, choice(rgb_colors))  # a filled circle dot

screen = Screen()
screen.exitonclick()
