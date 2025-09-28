from time import sleep
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake(shape="square", color="white")
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_on = True

while game_on:
    screen.update()
    sleep(0.1)

    snake.move()

    #Detect collusion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.ate = True
        snake.eat()
    else:
        snake.ate = False


screen.exitonclick()
