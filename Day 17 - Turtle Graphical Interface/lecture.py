from turtle import Turtle, Screen

# import turtle
# tim = turtle.Turtle()

# from turtle import *
#import everything from turtle module
#not recommended to be used
# turtle = Turtle()

#import turtle as t
# turtle = t.Turtle()

tim = Turtle()
tim.shape("turtle")
tim.color("green")

#challenge drawing a square
for _ in range(4):
    tim.forward(100)
    tim.right(90)

#creates a screen staying active until click
screen = Screen()
screen.exitonclick()
