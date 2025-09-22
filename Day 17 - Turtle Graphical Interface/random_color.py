import turtle as t
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color

tim = t.Turtle()
t.colormode(255)

tim.color(random_color())

screen = t.Screen()
screen.exitonclick()
