#functions

def my_function():
    print("My first function")

#Challenge: make robot to turn right
def turn_right():
    for _ in range(3):
        turn_left()
#Challenge: make robot draw a square
turn_left()
move()

for _ in range(3):
    turn_right()
    move()
