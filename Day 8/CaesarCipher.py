# Part 1

# Defining the alphabet list to be used for encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

# Taking user input for whether they want to encode or decode the message
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# Taking user input for the message to be encrypted or decrypted
text = input("Type your message:\n").lower()
# Taking user input for the number of shifts (the Caesar cipher key)
shift = int(input("Type the shift number:\n"))

# Function to encrypt a message using Caesar cipher
def encrypt(original_text, shift_amount):
    # Initializing an empty string for the cipher text
    cipher_text = ""
    # Looping through each letter in the original text
    for letter in original_text:
        # Finding the shifted position of the letter in the alphabet
        shifted_position = alphabet.index(letter) + shift_amount
        # Wrapping around the alphabet if the position exceeds the length
        shifted_position %= len(alphabet)
        # Adding the shifted letter to the cipher text
        cipher_text += alphabet[shifted_position]
    # Printing the encoded result
    print(f"Here is the encoded result: {cipher_text}")

# Calling the encrypt function with the provided text and shift amount
encrypt(original_text=text, shift_amount=shift)

# Part 2

# Redefining the alphabet list (same as before)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

# Taking inputs again for encoding/decoding, message, and shift number
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encrypt function (commented out as it's already implemented earlier)
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# Decrypt function (commented out, to be replaced by combined logic)
# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {cipher_text}")

# Combined Caesar cipher function for both encoding and decoding
def caesar(original_text, shift_amount, encode_or_decode):
    # Initializing an empty string for the output text
    output_text = ""
    # Adjusting the shift for decoding (shifting in the opposite direction)
    if encode_or_decode == "decode":
        shift_amount *= -1
    # Looping through each letter in the original text
    for letter in original_text:
        # Finding the shifted position of the letter and wrapping around the alphabet
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        # Adding the shifted letter to the output text
        output_text += alphabet[shifted_position]
    # Printing the final encoded/decoded result
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Calling the caesar function with the inputs
caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# Part 3
import art  # Importing art module (assuming it contains some ASCII art, like a logo)

# Displaying the logo (from the art module)
print(art.logo)

# Redefining the alphabet list (same as before)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

# Updated Caesar cipher function to handle non-alphabetic characters
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # Adjusting the shift amount for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Looping through each character in the input text
    for letter in original_text:
        # If the character is not in the alphabet, keep it unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # For alphabetic characters, find the shifted position and wrap it around
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            # Append the shifted letter to the output
            output_text += alphabet[shifted_position]
    # Print the final result
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Variable to control the loop
should_continue = True

# Running a loop to repeatedly ask for input and perform encoding/decoding
while should_continue:
    # Taking user inputs for direction, message, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Calling the caesar function with the provided inputs
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Asking if the user wants to continue
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    # If the user types 'no', exit the loop
    if restart == "no":
        should_continue = False
        print("Goodbye")
