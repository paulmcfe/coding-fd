# Import some libraries
import sys
import csv
import random

# Function to load words from a CSV file.
# It returns a list of dictionaries with the filtered words
def load_words(path):

    # Open the CSV file
    try:
        with open(path, newline='') as csv_file:

            # Read the CSV file into a dictionary
            # The keys are the column names and 
            # the values are the cell values
            reader = csv.DictReader(csv_file)
            
            # Filter the words based on the criteria
            # This list comprehension filters out words that are
            #     * Too short (less than 4 letters)
            #     * Too long (more than 10 letters)
            #     * Too obscure (Rank = 4)
            words = [row for row in reader 
                    if len(row['Word']) >= 4 
                    and len(row['Word']) <= 10 
                    and row['Rank'] != '4']

            # Return the list of word dictionaries
            return words
    except FileNotFoundError:
        print(f"Whoops! The file {path} wasn't found!")
        print("Make sure it's in the same folder as this script.")
        sys.exit()

# Get the list of words from the CSV file
# The file should be in the same directory as this script        
words = load_words('word_list.csv')

# Function to find anagrams of a word from a list of words
def find_anagrams(word, word_list):

    # Sort the letters of the word alphabetically
    sorted_word = ''.join(sorted(word.upper()))

    # The anagrams are all the words in the word list where
    # the Alpha key is the same as the word's sorted letters
    # The list comprehension also filters out the original word
    anagrams = [w['Word'] for w in word_list 
                if w['Alpha'] == sorted_word 
                and w['Word'] != word]

    # Return the list of anagrams
    return anagrams

# Print the welcome message
print("\n==============================")
print("    Welcome to Guessagram!")
print("==============================")
print("Your mission, should you choose to accept it, "
      "is to find all the anagrams of a random word.")
print("Some are easy. Some...not so much. Think you're up for the challenge?")
print("Type 'HINT' for a hint, or 'QUIT' to give up (no judgment...maybe).")
print("Let's twist some letters!\n")

# Run the main game loop
# The game continues until the user decides to quit
while True:
    # Get a random word
    # The word must have at least 3 anagrams
    random_word = random.choice([word['Word'] for word in words 
                                 if int(word['AnagramCount']) >= 3])

    # Find the anagrams of the random word
    anagrams = find_anagrams(random_word, words)

    # Print the word and the number of anagrams
    print(f"\nFind {len(anagrams)} anagrams of the word "
          f"'{random_word.upper()}':\n")
    
    # Initialize an empty list to store the guessed anagrams
    guessed = []

    # Track the number of guesses
    guesses = 0

    # Loop until all anagrams are guessed or the user quits
    while len(guessed) < len(anagrams):

        # Calculate the number of remaining anagrams
        remaining = len(anagrams) - len(guessed)

        # Prompt the user for a guess. The user can
        # enter a word, ask for a hint, or quit the game
        guess = input(f"Enter your guess ({remaining} left to find): ").strip().upper()

        # Increment the number of guesses
        if guess != "HINT" and guess != "QUIT":
            guesses += 1
        
        # Has the user already guessed this word?
        if guess in guessed:
            print("\nYou already guessed that one!\n")

        # Did the user guess an anagram?
        elif guess in [a.upper() for a in anagrams]:

            # If so, add it to the list of guessed anagrams
            guessed.append(guess)
            print("\nYes! Good one!\n")

        # Does the user want a hint?
        elif guess == "HINT":
            # Loop through the anagrams
            for a in anagrams:
                # If the anagram hasn't been guessed yet
                if a.upper() not in guessed:
                    # Print the anagram's first letter as a hint
                    print(f"\nPsst. One of the remaining anagrams starts with "
                            f"{a[0].upper()}.\n")
                    break

        # Does the user want to quit?
        elif guess == "QUIT":
            # If so, print a message and break out of the loop
            print("\nOkay, thanks for playing!\n")
            break

        # If we get this far, the 
        # guess was not an anagram
        else:
            print("\nNope, sorry. Please try again.\n")
        
        # Print the user's found anagrams (if any)
        if len(guessed) > 0:
            print("So far, you've found:")
            print(", ".join(guessed) + "\n")
 
    # Check if the user found all the anagrams
    if len(guessed) == len(anagrams):
        print(f"Great job! You found all {len(anagrams)} anagrams in "
            f"{guesses} guesses!\n")
        print("You are now officially an Anagram Wizard.\n")
    else:
        print("Guessagram wins this round. Better luck next time!\n")

        # Print the list of anagrams
        print("The anagrams were:")
        print(", ".join(anagrams) + "\n")

    # Ask the user if they want to play again.
    again = input("Do you want to play again? (y/n): ").strip().lower()
    
    # If the user doesn't want to play again, exit the game
    if again != 'y':
        print("\nOkay, see you. Thanks for playing!\n")
        break