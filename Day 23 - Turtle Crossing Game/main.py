import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def player_hit_car(pl, cars):

    for car in cars:
        if pl.distance(car) < 20:
            return True
    return False

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#initialize player
player = Player()

#player controls
screen.listen()
screen.onkey(fun=player.move, key="Up")

#scoreboard
scoreboard = Scoreboard()

#car manager
car_manager = CarManager()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create and move cars
    car_manager.create_car()
    car_manager.cars_move()

    #Detect collusion with player
    if player_hit_car(pl=player, cars=car_manager.cars):
        scoreboard.game_over()
        game_is_on = False

    #player crosses finish line
    if player.is_at_finish_line():
        scoreboard.level_up()
        player.reset_position()
        car_manager.increase_speed()

screen.exitonclick()
