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
    scoreboard.increase_score()
    snake.ate = True
    snake.grow()
  else:
      snake.ate = False

  #Detect collusion with wall
  if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or \
    snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
    scoreboard.game_over()
    game_on = False

  #Detect collusion with tail

  if snake.tail_collusion():
    scoreboard.game_over()
    game_on = False

screen.exitonclick()
