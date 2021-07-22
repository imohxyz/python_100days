def turn_right():
    turn_left()
    turn_left()
    turn_left()
def aa():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
# using foor
#for f in range(6):
#    aa()
# using while cara lama
#belokan = 6
#while belokan > 0:
#    aa()
#    if at_goal():
#        belokan = 0
#    else:
#        belokan -= 1
# using while cara cepet
while not at_goal():
    aa()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
