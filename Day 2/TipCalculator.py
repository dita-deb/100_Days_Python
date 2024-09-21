# Tip Calculator

# Welcome message
print("Welcome to the tip calculator!")

# Input: Get the total bill amount from the user as a floating-point number
bill = float(input("What was the total bill? $"))

# Input: Get the percentage of the tip the user wants to give (10, 12, or 15)
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))

# Input: Get the number of people to split the bill between
people = int(input("How many people to split the bill? "))

# Calculate the total bill including the tip
bill_with_tip = tip / 100 * bill + bill

# Calculate how much each person should pay
bill_per_person = bill_with_tip / people

# Output: Print the total bill including the tip, rounded to 2 decimal places
print(round(bill_with_tip, 2))

# Output: Print how much each person needs to pay, rounded to 2 decimal places
print(round(bill_per_person, 2))

