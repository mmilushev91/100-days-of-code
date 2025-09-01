def turn_right():
    for _ in range(3):
        turn_left()
def step_over():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
steps = 6

for _ in range(steps):
    step_over()
