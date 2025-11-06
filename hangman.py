import random
import string

tries = 6
# List with random words to guess from
words = ["banana", "chocolate", "watermelon", "cranberry", "bagel"]
# Choose a word with a random index from the list
word = words[random.randint(0, len(words)-1)]
guessed_letter = ""
guessed_letters = []

# Populate the list with the right number of underscores to display the guessed word in real time
guessed_word = []
for i in range (0, len(word)):
    guessed_word.append("_")
    
print(" ".join(guessed_word))

# Run while loop until we guess the entire word or run out of tries by guessing the wrong letters
while tries > 0:
    # Print all previously guessed letters out, only if list isn't empty
    if guessed_letters != []:  
        print(f"Your guessed letters: {", ".join(guessed_letters)}")
    
    # Input for player to guess letters
    guessed_letter = input(f"You have {tries} tries left.\nGuess a letter: ").lower()
    
    # Don't allow to guess previously guessed letters again
    if guessed_letter in guessed_letters:  
        print(f"You already guessed this letter, try a different one!\n{" ".join(guessed_word)}")
        continue
    
    # Don't allow numbers, special characters or longer strings
    if len(guessed_letter) != 1 or guessed_letter not in string.ascii_lowercase:
        print(f"Please enter a single letter.\n\n{" ".join(guessed_word)}")
        continue
    
    # Deduct number of tries left on bad guesses, add guessed letter to list
    if guessed_letter not in word:
        tries -= 1
        guessed_letters.append(guessed_letter)
        if tries == 0:
            print(f"Game over! You ran out of tries! The guessed word was {word}")
            break
        print(f"Letter {guessed_letter} is not in the word. Try again.\n\n{" ".join(guessed_word)}")
    
    # Write the correctly guessed letter in the right position instead of an underscore, add guessed letter to list
    else:
        x = 0
        while x < len(word):
            if word[x] == guessed_letter:
                guessed_word[x] = guessed_letter
            x += 1
        print(" ".join(guessed_word))
        guessed_letters.append(guessed_letter)
    
    # Win condition  
    # Print word with .join() to make it look like a string not list
    if "".join(guessed_word) == word:
        print(f"Congratulations! You guessed the word {"".join(guessed_word)}!")
        break