import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password = ""
# for char in range(0, nr_letters):         #simplify the range for items in the specified list
#     password += random.choice(letters)    #choose random amount of letters (based on user input) and adding it existing pw
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)    #choose random amount of symbols (based on user input) and adding it existing pw
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)    #choose random amount of numbers (based on user input) and adding it existing pw
#
# print(password)                           #simpliest form which is not the most secure

# Hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

#print(password_list)                       #prints characters in list in the sections orderly (like easy mode)
random.shuffle(password_list)               #shuffles the characters in the list
#print(password_list)                       #prints the shuffled list

password = ""
for char in password_list:                  #converting back into a string using a for loop
    password += char

print(f"Your password is: {password}")      #prints the final shuffled string password

