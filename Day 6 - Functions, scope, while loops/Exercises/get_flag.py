def turn_right():
    for _ in range(3):
        turn_left()
def step_over():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
steps = 5
move()

for _ in range(steps):
    step_over()
    turn_left()
    move()

step_over()
