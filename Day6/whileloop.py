def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_square():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    one_square()

#We use while loop when we have a condition to check and not number to count


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        one_square()
    else:
        move()