#Functions with Outputs
# Function to format the first and last name properly
# It capitalizes the first letter of each name and returns the formatted full name
def format_name(f_name, l_name):
    # Capitalize the first letter of the first and last name
    formated_f_name = f_name.title()  # Converts the first name to title case
    formated_l_name = l_name.title()  # Converts the last name to title case
    # Return the formatted full name
    return f"{formated_f_name} {formated_l_name}"

# Example of calling the format_name function
print(format_name("aninDITA", "deb"))  # Output will be "Anindita Deb"

# Function that duplicates the input text
def function_1(text):
    # Return the text concatenated with itself
    return text + text

# Function that capitalizes the first letter of each word in the text
def function_2(text):
    # Converts the entire text to title case
    return text.title()

# Nested function call: function_1 will duplicate the text, and then function_2 will capitalize it
output = function_2(function_1("hello"))  # Output will be "Hello Hello"
print(output)


#Multiple Return Values
# Function to format the first and last name properly
# It returns a formatted full name or a message if inputs are invalid
def format_name(f_name, l_name):
    # Check if either the first name or last name is empty
    if f_name == "" or l_name == "":
        # Return a message indicating invalid input if any name is missing
        return "You did not provide valid inputs"
    
    # Capitalize the first letter of each name and make the rest of the letters lowercase
    formated_f_name = f_name.title()  # Title case the first name
    formated_l_name = l_name.title()  # Title case the last name
    
    # Return the formatted full name with a label
    return f"Result: {formated_f_name} {formated_l_name}"

# Prompt the user for their first and last name, format it, and print the result
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Leap Year
def is_leap_year(year):
    """
    This function takes a year as input and returns True if it is a leap year,
    otherwise returns False.
    
    A year is a leap year if:
    - It is divisible by 4, but not divisible by 100, OR
    - It is divisible by 400.
    
    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    # Check if the year is divisible by 400 (leap year)
    if year % 400 == 0:
        return True
    # If not divisible by 400, check if it is divisible by 100 (not a leap year)
    elif year % 100 == 0:
        return False
    # If not divisible by 100, check if it is divisible by 4 (leap year)
    elif year % 4 == 0:
        return True
    # If not divisible by 4, it is not a leap year
    else:
        return False

# Test cases
print(is_leap_year(2400))  # Output: True
print(is_leap_year(1989))  # Output: False
print(is_leap_year(2000))  # Output: True
print(is_leap_year(2100))  # Output: False


#Docstrings
# Function to format the first and last name with a docstring explaining its purpose
def format_name(f_name, l_name):
    """
    Take a first and last name and format them by converting both to title case.
    
    Args:
    f_name (str): The first name to be formatted.
    l_name (str): The last name to be formatted.
    
    Returns:
    str: The formatted full name in title case.
    """
    # Convert the first and last name to title case (first letter capitalized, rest lowercase)
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    # Return the formatted full name as a single string
    return f"{formated_f_name} {formated_l_name}"

# Call the function to format the name "Anindita Deb"
formatted_name = format_name("anInDITa", "DEB")

# Calculate the length of the formatted full name
length = len(formatted_name)



