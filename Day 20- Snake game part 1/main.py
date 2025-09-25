from turtle import Screen
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake(shape="square", color="white")
snake.create_snake()

screen.onkeypress(fun=snake.move_left, key="a")
screen.onkeypress(fun=snake.move_right, key="d")

game_on = True

while game_on:
  screen.update()
  sleep(0.1)
  
  snake.snake_move()

screen.exitonclick()
