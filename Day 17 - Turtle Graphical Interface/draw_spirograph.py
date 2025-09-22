import turtle as t
from random import randint

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    color = (r, g, b)
    return color

def draw_spirograph(step):
    for angle in range(0, 360, step):
        # change heading
        tim.setheading(angle)
        # change color
        tim.color(random_color())
        # draw circle
        tim.circle(radius=100)

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
