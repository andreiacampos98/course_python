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

def move_all():
    for i in range(1,7):
        one_square()
 
move_all()