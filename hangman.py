import random
import string

tries = 6
# List with random words to guess from
words = ["banana", "chocolate", "watermelon", "cranberry", "bagel"]
# Choose a word with a random index from the list
word = words[random.randint(0, len(words)-1)]
print(word) #---------debug
guessed_letter : str = ""
guessed_letters = []
guessed_word = []
# Populate the list with the right number of underscores
for i in range(0, len(word)):
    guessed_word.append("_")

while tries > 0:  # Run while loop until we guess the entire word or run out of tries by guessing the wrong letters
    # Print word with .join() to make it look like a string not list
    if "".join(guessed_word) == word:
        print(f"Congratulations! You guessed the word {"".join(guessed_word)}!")
        break
    if guessed_letters != []:  # Print all previously guessed letters out, only if list isn't empty
        print(f"Your guessed letters: {", ".join(guessed_letters)}")  # Formatting
    guessed_letter = input(f"You have {tries} tries left.\nGuess a letter: ").lower()  # Input for player to guess letters
    # After guessing letter:
    if (len(guessed_letter)) == 1 and guessed_letter in string.ascii_lowercase:  # Check if length of entered string is 1 and a letter
        #string.ascii_letters is a string that contains all the uppercase and lowercase letters(abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ). Using lowercase only since I already convert it
        if guessed_letter in guessed_letters:  # Don't allow to guess previously guessed letters again
            print("You already guessed this letter, try a different one!\n")
        elif guessed_letter in word:
            print(f"Letter {guessed_letter} is correct!\n")
            # Cross out and display guessed letter
            x : int = 0
            while x < len(word):
                if word[x] == guessed_letter:  # Write the correctly guessed letter in the right position instead of an underscore
                    guessed_word[x] = guessed_letter  # So here I've learned that strings in Python are immutable lol that explains everything. Changed to list to get indexes
                x += 1
            print("".join(guessed_word))
            guessed_letters.append(guessed_letter)  # Add letter to already guessed list
        else:
            # Deduct number of tries left if incorrect
            tries -= 1
            print(f"Letter {guessed_letter} is not in the word. Try again.\n\n{"".join(guessed_word)}")
            guessed_letters.append(guessed_letter)  # Add letter to already guessed list
    else:
        print(f"Please enter a single letter.\n\n{"".join(guessed_word)}")  # Don't need else since we have break above
print(f"Game over! You ran out of tries! The guessed word was {word}")


'''
while tries > 0
input letter
check if letter ==1
check if letter was already guessed previously
check if letter in word and display it instead of underscore - add letter to guessed letters
else if letter not in word deduce tries - add letter to guessed
else enter a single char ==1
else game over

print all guessed letters every iteration
don't allow special characters/numbers
'''