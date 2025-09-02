def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
