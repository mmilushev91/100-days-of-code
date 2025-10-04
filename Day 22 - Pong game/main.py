from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

PLAYER_1_START_X = -350
PLAYER_2_START_X = 350

# Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Create paddles
player_1 = Paddle(start_x=PLAYER_1_START_X)
player_2 = Paddle(start_x=PLAYER_2_START_X)

# Create ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Move paddles
screen.listen()
screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.up, key="Up")
screen.onkey(fun=player_2.down, key="Down")

game_on = True
sleep_time = 0.1

while game_on:

    sleep(sleep_time)
    screen.update()
    # Move the ball
    ball.move()

    # Detect colusion with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect colusion with paddle
    if ball.distance(player_1) <= 50 and ball.xcor() < -320 or \
            ball.distance(player_2) <= 50 and ball.xcor() > 320:
        ball.bounce_x()
        sleep_time -= 0.01

    # Detect when paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_player1_score()
        ball.reset()
        sleep_time = 0.1
    elif ball.xcor() < -350:
        scoreboard.increase_player2_score()
        ball.reset()
        sleep_time = 0.1

screen.exitonclick()
