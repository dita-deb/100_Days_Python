# Step 1
import random

# List of words for the game
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Print the chosen word to show the current word for debugging purposes.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2: Ask the user to guess a letter and assign their answer to a variable called guess.
# The input is converted to lowercase to ensure case-insensitive comparisons.
guess = input("Guess a letter: ").lower()

# TODO-3: Check if the letter the user guessed is one of the letters in the chosen_word.
# Print "Right" if the guess is correct, otherwise print "Wrong".
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# Step 2
import random

# Word list for the game
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" string with the same number of underscores as the length of the chosen_word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Ask the user to guess a letter and convert it to lowercase
guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that places the guessed letter in the correct positions and 
# underscores in the rest of the places.
display = ""

# Loop through each letter in the chosen_word
for letter in chosen_word:
    # If the guessed letter matches, add it to the display
    if letter == guess:
        display += letter
    else:
        display += "_"

# Print the current display with correct guesses and blanks
print(display)

# Step 3
import random

# Word list for the game
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

# Create a placeholder string with underscores for each letter in the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Variable to track if the game is over
game_over = False

# List to keep track of correctly guessed letters
correct_letters = []

# Main game loop, runs until the game is over
while not game_over:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # String to display the current word with guessed letters and underscores
    display = ""

    # Loop through each letter in the chosen_word
    for letter in chosen_word:
        # If the guessed letter matches, add it to the display and the correct_letters list
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        # If the letter was previously guessed correctly, add it to the display
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Print the current state of the display
    print(display)

    # Check if the entire word has been guessed
    if "_" not in display:
        game_over = True
        print("You win.")

# Step 4
import random

# Stages of the hangman figure for incorrect guesses
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Word list for the game
word_list = ["aardvark", "baboon", "camel"]

# Number of lives or incorrect guesses allowed
lives = 6

# Randomly select a word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

# Display a placeholder with underscores for each letter in the word
word_length = len(chosen_word)
placeholder = "_" * word_length
print(placeholder)

# Variable to track if the game is over
game_over = False

# List to store correctly guessed letters
correct_letters = []

# Main game loop, runs until the game is over
while not game_over:
    # Ask the user to guess a letter and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # String to display the current state of the word with correct guesses
    display = ""

    # Loop through each letter in the chosen_word
    for letter in chosen_word:
        # If the guessed letter is correct, add it to the display and correct_letters list
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        # If the letter was guessed correctly earlier, add it to the display
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Print the current display of the word
    print(display)

    # If the guessed letter is not in the chosen word, reduce the number of lives
    if guess not in chosen_word:
        lives -= 1
        # If lives run out, the player loses
        if lives == 0:
            game_over = True
            print("You lose.")

    # Check if the player has won by guessing all the letters
    if "_" not in display:
        game_over = True
        print("You win.")

    # Print the current hangman stage based on remaining lives
    print(stages[lives])
