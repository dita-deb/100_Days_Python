# Importing the necessary modules and variables
import random

# Import word list and hangman stages/graphics from external files
from hangman_words import word_list
from hangman_art import stages, logo

# Initial number of lives or incorrect guesses allowed
lives = 6

# Display the hangman game logo
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
print(chosen_word)  # Print the chosen word for debugging (can be removed for actual gameplay)

# Create a placeholder string of underscores with the same length as the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)  # Display the word with underscores initially

# Variable to track if the game is over
game_over = False

# List to keep track of correctly guessed letters
correct_letters = []

# Main game loop that runs until the game is over
while not game_over:

    # Display the current number of lives left
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    
    # Ask the user to guess a letter and convert it to lowercase
    guess = input("Guess a letter: ").lower()

    # If the letter has already been guessed, inform the user
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Variable to store the current state of the word (with guessed letters and underscores)
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
        # Otherwise, add an underscore to the display
        else:
            display += "_"

    # Print the current state of the word
    print("Word to guess: " + display)

    # If the guessed letter is not in the chosen word, reduce the number of lives
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        # If lives run out, the player loses the game
        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # Check if the player has won by guessing all the letters
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print the current hangman stage based on the number of remaining lives
    print(stages[lives])
    
