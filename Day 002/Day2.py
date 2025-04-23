# Data Types
# - Strings
print(len("Hello"))  #will display the length of Hello which is 5
print("Hello"[4])    #Will display the character 'o' from the string starting at 0
print("Hello"[-1])   #get hold of the last character in the string which is 'o'
print("123"+"345")   #will display 123345 not actually calculating the operation; simply concatenate 
# - Integers
print(123+345)       #Whole number operations
print(123,456,789)   #Display segmented integers
print(123456789)     #Display large whole numbers
print(123_456_789)   #Display large integers that are more readable
# - Floats
print(3.14159)       #Known as a floating point number
# - Booleans
print(True)
print(False)

# Type Error, Checking and Conversion
#len(12345) is a type error because len can not measure the objects inside an integer, it can for strings though
print(type("Hello"))  #check the data type and prints it to console: <class 'str'>
print(type(123))  #check the data type and prints it to console: <class 'int'>
print(type(3.14))  #check the data type and prints it to console: <class 'float'>
print(type(True))  #check the data type and prints it to console: <class 'bool'>
#now what if I don't like the data type and want to convert it:
print("123"+"345")              #This again just concatenates
print(int("123")+int("345"))    #This converts the string "123" and "345" into integers 123 and 345 producing 468
#print(int("abc")+int("345"))   #abc conversion into int is met with a value error;
                                # default str abc can't be added to int 356

name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name:"))  #str
print(type(length_of_name))                     #int

print("Number of letters in your name: " + str(length_of_name))     #making the appropriate conversion of int to str 

# Mathematical Operations
# - Basic Operations:
print("My age: " + str(12))
print(123+456)  #addition
print(7-3)      #substraction
print(3*2)      #multiplication
print(6/3)      #division results into a floating point number 2.0
print(6//3)     #division results in an integer 2 (does the division like previous line, but removes decimals)
print(2**3)     #exponents: 2^3 = 8
# - PEMDAS (LR - Left to Right)
# () THEN ** THEN [ * OR / ] THEN [ + OR - ]
print(3*3+3/3-3)    #gets 7.0
print(3*(3+3)/3-3)  #gets 3.0


#BMI calculator
#given weight and height
#defined height and weight
height = 1.65  # in meters
weight = 84    # in kilograms
# Calculate the BMI
bmi = weight / (height ** 2)  # bmi is equal to the person's weight divided by the person's height squared
# Output the BMI
print(bmi)

#Number Manipulation
bmi = 84 / 1.65 ** 2
print(bmi)          #30.85399449035813
print(int(bmi))     #30
# - Rounding a Number
print(round(bmi))   #31
print(round(bmi,2)) #30.85
# - Assignment Operations
# += will add the number on the right to the original value
# of the var on the left and assign the new value to the var
score = 0
score += 1
print(score)
# -= will sub the number on the right to the original value
# of the var on the left and assign the new value to the var
passes = 0
passes -= 1
print(passes)
# *= will multiply the number on the right to the original value
# of the var on the left and assign the new value to the var
num = 1
num *= 2
print(num)
# /= will divide the number on the right to the original value
# of the var on the left and assign the new value to the var
num = 1
num /= 2
print(num)
# - f-Strings
score = 0
height =1.0
is_winning = True

print(f"Your score is = {score}, your height is {height}. You're winning is {is_winning}")
#cut down on a lot of manual labor in converting a lot of the data types into strings for displaying

