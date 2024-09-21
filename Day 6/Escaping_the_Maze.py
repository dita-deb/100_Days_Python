def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()     # move till it finds a wall
turn_left()    # turn so that the wall is on the right #additionally we leave that while loop

while not at_goal():    #now we finally have a wall on the right to enter this while loop
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

## Day 15 --come back to this for the problem worlds
