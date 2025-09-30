from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

PLAYER_1_START_X = -350
PLAYER_2_START_X = 350

#Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

#Create paddles
player_1 = Paddle(start_x=PLAYER_1_START_X)
player_2 = Paddle(start_x=PLAYER_2_START_X)

#Create ball
ball = Ball()

#Create scoreboard
scoreboard = Scoreboard()

#Move paddles
screen.listen()
screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.up, key="Up")
screen.onkey(fun=player_2.down, key="Down")

game_on = True

while game_on:
  sleep(0.1)
  #Move the ball
  ball.move()

  #Detect colusion with wall and bounce

screen.exitonclick()


#Detect colusion with paddle
#Detect when paddle misses
#Keep score
