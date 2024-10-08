# If-Else and other comparator operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:                                       #if <this condition is true>:
    print("You can ride the rollercoaster!")            #<then execute this line of code>
else:                                                   #if <this condition is false>:
    print("Sorry you cannot ride the roller coaster.")  #<then execute this line of code>
# - Comparator Operators
# > Greater than , < Less than, >= Greater than or equal to, <= Less than or equal to, == Equal to, != Not equal to

# Modulo Operator - returns the remainder of a division between two numbers
print(6 % 2) #will be 0
print(6 % 5) #will be 1
print(6 % 4) #will be 2

# - Even or Odd Checker:
num = int(input("What is the number you want to check: "))

if num % 2 == 0:                              #checks for remainders
    print(f"Your number, {num}, is even.")    #if no remainder it is even
else:
    print(f"Your number, {num}, is odd.")     #else is odd

# Nesting and Elif
# For Nested condtitions look at the larger condition first before digging deeper into another condition inside the first
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:                                                   #Condition #1
    print("You can ride the rollercoaster")                         #if condition 1 is true you can continue to nested loop
    age = int(input("What is your age? "))
    if age <= 12:                                                   #nested elif loop: condition #2
        print("Please pay $5.")                             
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")                            
else:
    print("Sorry you have to grow taller before you can ride.")     #Condition #1 False statement

# BMI exercise.py
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi <18.5:            #If the bmi is under 18.5 (not including), print out "underweight"
    print("underweight")  
elif bmi <25:            #If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
    print("normal weight")
else:                    #If the bmi is 25 (including) or over, print out "overweight"
    print("overweight")

# Multiple Ifs
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:                          #This is the first nested if-statement.      
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. ")
    if wants_photo == "y":                 #This If-statement follows the next if statement in the same indent
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")

# Python Pizza Delivery 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":             #First check the size conditions
    bill =15
elif size == "M":
    bill =20
else:
    bill =25

if pepperoni == "Y":
    if size == "S":         #Size s pepperoni is different than m and l
        bill += 2
    else:                   #Pepperoni on M and L options
        bill += 3

if extra_cheese == "Y":     #Extra cheese on any pizza size
    bill += 1

print(f"Your final bill is: ${bill}.")

#Multiple Conditions and Logical Operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:       #multiple conditions can also be ( 45<= age >=55 )
        print("Everything is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

