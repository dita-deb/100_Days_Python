#got bored so I made this for funsies

def pig_latin_translator():
    # Step 1: Ask the user to input a word
    word = input("Enter a word in English: ").strip()
    
    # Step 2: Check if the user entered a valid word
    if not word.isalpha() or len(word) == 0:
        print("Invalid input. Please enter a valid word consisting of letters only.")
        return
    
    # Step 3: Convert the word from English to Pig Latin
    # Ensure the word is in lowercase for uniformity
    word = word.lower()
    pig_latin_word = word[1:] + word[0] + "ay"
    
    # Step 4: Display the translation result
    print(f"The word in Pig Latin is: {pig_latin_word}")

# Run the Pig Latin translator
pig_latin_translator()
