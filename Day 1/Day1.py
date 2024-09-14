#Printing
print("Hello world!")

#String Manipulation
#Part 1:
print("Hello world!\nHello world!\nHello world!")
#Part 2:
print("Hello" + " " + "Dita")

#Inputs
# We are concatenating the input inside the printing function. We simplify the entire code that way to display
# both the question for inout and its output depending on its entered information.
print("Hello " + input("What is your name? ") + "!")

#Variables:
#Printing the length of the received input for the question below.
print(len(input("What is your name? ")))
#breaking it down into more lines of code can be a good way to keep track of documentation/definitions 
username = input("What is your name? ")
length = len(username)
print(length)

##Switching variables displays the glasses with switched contents without typing them out
glass1 = "milk"
glass2 = "juice"
glass1, glass2 = glass2, glass1

#Naming Variables
name = "Dita"  #want to have meaningful named variables to look back onto otherwise confusion
length = len(name)
print(length)  #commenting code would be a good habit to have as well


#Band Name Generator 
#Building the Band Generator
print("Welcome to Band Name Generator!")                    #Print welcome prompt
city = input("What's the name of city you grew up in?\n")   #define the input as a variable city
pet_name= input("What's your pet's name?\n")                #define the input as a variable pet_name
print("Your band name could be " + city + " " + pet_name)   #concatente city and pet_name into the displayed result

