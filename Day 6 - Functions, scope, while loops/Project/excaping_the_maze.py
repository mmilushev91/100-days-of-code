def turn_right():
    for _ in range(3):
        turn_left()

def turn_north():
    while not is_facing_north():
        turn_left()
        
turn_north()

while not at_goal():
    
    if right_is_clear():
        turn_right()
    else:
        while not front_is_clear():
            turn_left()
    move()
    
