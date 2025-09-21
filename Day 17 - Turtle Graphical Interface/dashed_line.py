from turtle import Turtle, Screen

#challenge make a dashed line

def draw_dashed_line(step_length, line_length, line):
    for i in range(line_length):
        line.penup() if i % 2 != 0 else line.pendown()
        line.forward(step_length)

dashed_line = Turtle()
draw_dashed_line(step_length=10, line_length=15, line=dashed_line)
