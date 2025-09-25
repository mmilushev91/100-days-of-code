from turtle import Turtle

class Snake:

  def __init__(self, shape, color) -> None:
    self.shape = shape
    self.color = color 
    self.snake = []
    self.snake_head = None

  def create_snake_segment(self):
    segment = Turtle(shape=self.shape)
    segment.color("white")
    segment.penup()
    
    return segment

  def create_snake(self) -> None:
  
    for x in range(0, -60, -20):
      segment = self.create_snake_segment()
      segment.setx(x)
      self.snake.append(segment)

    self.snake_head = self.snake[0]

  def snake_move(self) -> None:
    snake_body_last_index = len(self.snake) - 1

    for i in range(snake_body_last_index, 0, -1):
      new_x_cord = self.snake[i - 1].xcor()
      new_y_cord = self.snake[i - 1].ycor()

      self.snake[i].goto(new_x_cord, new_y_cord)

    self.snake[0].forward(20)

  def move_up(self):
    self.snake_head.setheading(self.snake_head.heading() + 90)
  def move_left(self):
    self.snake_head.setheading(self.snake_head.heading() + 90)

  def move_right(self):
    self.snake_head.setheading(self.snake_head.heading() - 90)
