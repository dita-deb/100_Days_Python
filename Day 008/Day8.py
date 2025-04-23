# Functions with Inputs
#Simple Function that packages code into a named block
def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice?")


greet()

# Life in Weeks
def life_in_weeks(age):
    #Total lifespan in weeks (90 years * 52 weeks per year)
    total_weeks = 90 * 52
    
    #Weeks lived so far
    weeks_lived = age * 52
    
    #Weeks left to live
    weeks_left = total_weeks - weeks_lived
    
    #Output the result with proper formatting
    print(f"You have {weeks_left} weeks left.")

#Test the function with a hard-coded value
life_in_weeks(56)

# Positional vs Keyword Arguments
#Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Billie")

#Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional arguments
#greet_with("Jack Bauer", "Nowhere")
#greet_with("Nowhere", "Jack Bauer")


# Keyword arguments
greet_with(location="London", name="Angela")

# Love Calculator
def calculate_love_score(name1, name2):
    # Combine both names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Define the letters for 'TRUE' and 'LOVE'
    true_letters = "true"
    love_letters = "love"

    # Count occurrences of each letter in 'TRUE'
    true_count = 0
    for letter in true_letters:
        true_count += combined_names.count(letter)

    # Count occurrences of each letter in 'LOVE'
    love_count = 0
    for letter in love_letters:
        love_count += combined_names.count(letter)

    # Combine both counts into a two-digit number as a string
    love_score = int(str(true_count) + str(love_count))

    # Print the final love score
    print(love_score)

# Test the function with the provided example
calculate_love_score("Kanye West", "Kim Kardashian")

