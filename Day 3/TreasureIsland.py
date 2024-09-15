from random import choice

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#3 ''' are a great way to print multiple lines as strings
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroads where do you want to go? '
                'Type "left" or "right". ').lower()

if choice1 == "left" or choice1 == "Left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
          'Type "wait" to wait for a boat or "swim" to swim across. ').lower()
    if choice2 == "wait" or choice2 == "Wait":
        choice3 = input('You\'ve arrived at the island unharmed.'
                        'There is a house with 3 doors:'
                        '\nOne Red, One Yellow, One Blue.'
                        '\nwhich color do you choose? ').lower()
        if choice3 == "red" or choice3 == "Red":
            print("It's a room full of fire.\nGame Over.")
        elif choice3 == "yellow" or choice3 == "Yellow":
            print("You found the treasure!\nYou Win!")
        elif choice3 == "blue" or choice3 == "Blue":
            print("You entered a room of beast.\nGame Over.")
        else:
            print("You chose a door that doesn't exist.\nGame Over.")
    else:
        print("You got attacked by an angry trout.\nGame Over.")
else:
    print("You fell into a hole.\nGame Over.")
