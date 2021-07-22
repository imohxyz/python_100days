def turn_right():
    turn_left()
    turn_left()
    turn_left()
def aa():
    turn_left()
    move()
while not at_goal():
    if right_is_clear():
        turn_right()
    if wall_in_front():
        if right_is_clear():
            aa()
        else:
            turn_left()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
