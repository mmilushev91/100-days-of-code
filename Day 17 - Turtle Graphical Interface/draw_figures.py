from turtle import Turtle, Screen
from random import choice

def generate_random_color(colors):
    return choice(colors)

turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "black", "white", "brown", "gray", "cyan", "magenta", "gold",
    "silver", "violet", "indigo", "lime", "turquoise", "navy",
    "maroon", "beige", "tan", "chocolate", "coral", "salmon"
]

circle_degrees = 360
side_length = 100
start_figure_sides = 3
end_figure_sides = 10

draw_line = Turtle()

for i in range(start_figure_sides, end_figure_sides + 1):
    degrees = circle_degrees / i
    draw_line.color(generate_random_color(colors=turtle_colors))

    for j in range(i):
        draw_line.forward(side_length)
        draw_line.right(degrees)






screen = Screen()
screen.exitonclick()
