from turtle import Turtle

SNAKE_PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, shape, color) -> None:
        self.shape = shape
        self.color = color
        self.snake = []
        self.create()
        self.head = self.snake[0]
        self.ate = False

    def create_snake_segment(self):
        segment = Turtle(shape=self.shape)
        segment.penup()
        segment.speed("fastest")

        return segment

    def create(self) -> None:

        for x in range(0, -60, -20):
            segment = self.create_snake_segment()
            segment.color("white")
            segment.setx(x)
            self.snake.append(segment)

    def move(self) -> None:
        snake_body_last_index = len(self.snake) - 1

        if self.ate:
            self.snake[snake_body_last_index].color("white")

        for i in range(snake_body_last_index, 0, -1):
            new_x_cord = self.snake[i - 1].xcor()
            new_y_cord = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x_cord, new_y_cord)

        self.head.forward(SNAKE_PACE)

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat(self):
        self.snake.append(self.create_snake_segment())


