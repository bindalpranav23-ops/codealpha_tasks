import random  # random module import kiya for random word selection

# List of 5 predefined words for the game
words = ["python", "hangman", "code", "laptop", "github"]

# Randomly pick one word from the list
actual_word = random.choice(words)

# Create a list of underscores, one for each letter in the word
guessed_word = []
for i in range(len(actual_word)):
    guessed_word.append("_")

# Counter to track wrong guesses (max allowed: 6)
wrong_guesses = 0

# List to keep track of letters already guessed
guessed_letters = []

# Game loop: runs until word is fully guessed OR wrong guesses reach 6
while "".join(guessed_word) != actual_word and wrong_guesses < 6:
    
    # Show current progress (e.g., c _ d _)
    print(" ".join(guessed_word))
    
    # Take input letter from player
    guess = input("Enter a letter: ")
    
    # Check if the guessed letter exists in the word
    if guess in actual_word:
        # Loop through the word to find and update the correct position(s)
        for i in range(len(actual_word)):
            if actual_word[i] == guess:
                guessed_word[i] = guess
    else:
        # Wrong guess, increase the counter
        wrong_guesses = wrong_guesses + 1

# After the loop ends, check if the player lost or won
if wrong_guesses == 6:
    print("Tum haar gaye! Sahi word tha:", actual_word)
else:
    print("Tum jeet gaye! 🎉")
