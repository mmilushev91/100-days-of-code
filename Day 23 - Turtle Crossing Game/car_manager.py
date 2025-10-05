from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 300
START_RANDOM_Y = (-250, 250)

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)

        if random_chance == 1:
            car = Turtle(shape="square")
            car.color(choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y_start, random_y_end = START_RANDOM_Y
            car.goto(x=START_X, y=randint(random_y_start, random_y_end))
            self.cars.append(car)

    def cars_move(self):

        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
