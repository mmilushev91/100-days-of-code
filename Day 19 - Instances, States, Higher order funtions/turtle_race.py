from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make your bet",
                 prompt="Which turtle will won the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def start_line():
    x = -230 
    y = -70

    turtles = []
    for color in colors:
        current_turtle = Turtle("turtle")
        current_turtle.color(color)
        current_turtle.penup()
        current_turtle.goto(x= x, y= y)
        y += 30
        turtles.append(current_turtle)

    return turtles
                 
def turtle_race():
    all_turtles = start_line()
    game_on = True 
                 
    while game_on:
                 
        for current_turtle in all_turtles:
            random_step = randint(1, 10)
            current_turtle.forward(random_step)

            if current_turtle.xcor() >= 230:
                game_on = False
                winner = current_turtle.fillcolor()
                screen.bye()
                print(f"{winner.title()} turtle is the winner!")
                print("You win" if winner == user_guess else "You lose" + "!")
                break

turtle_race()
