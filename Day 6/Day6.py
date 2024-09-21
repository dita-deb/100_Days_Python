def my_function():
    print("Hello")
    print("Bye")


my_function()   #improves the overall readability of codewill print all parts of this function line by line

#the next part of this course actually utilizes Reeborg's World to help practice functions

# First reeborg's world problem I didn't document it but the robot makes a square on the grid.
#essentially just making turn_right function with the basic building blocks move() and turn_left()

# Hurdles Loop challenge
#This was my attempt at the hurdles challenge that ran successfully
def turn_right():        #Defining the function to turn right
    turn_left()
    turn_left()
    turn_left()
    
def jump():              #making the jump function
    move()
    turn_left()
    move()
    turn_right()         #first right turn
    move()
    turn_right()         #over the first hurdle now going back down
    move()
    turn_left()          #back in starting position for the next hurdle

for every_hurdle in range(6):        #for loop in the range of every hurdle simplifies calling the jump() function 6 times
    jump()

# Indentation
#I think this should have been an earlier lesson for coding with loops, if-else, conditionals, and functions
#Indentation is 4 spaces to 1 tab

# While Loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)        #checks condition of whether the number_of_hurdles is still > 0

#at_goal condition while loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():                #while not at goal perform jump
    jump()


# Hurdle #3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump() 
    else:
        move()

# Hurdle #4
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump() 
    else:
        move()

