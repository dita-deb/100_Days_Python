# Functions with Inputs
#Simple Function that packages code into a named block
def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice?")


greet()

# Life in Weeks
def life_in_weeks(age):
    # Total lifespan in weeks (90 years * 52 weeks per year)
    total_weeks = 90 * 52
    
    # Weeks lived so far
    weeks_lived = age * 52
    
    # Weeks left to live
    weeks_left = total_weeks - weeks_lived
    
    # Output the result with proper formatting
    print(f"You have {weeks_left} weeks left.")

# Test the function with a hard-coded value
life_in_weeks(56)


#Function that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Billie")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional arguments
# greet_with("Jack Bauer", "Nowhere")
# greet_with("Nowhere", "Jack Bauer")


# Keyword arguments
greet_with(location="London", name="Angela")


