# Hangman game
With this project I've strengthened my knowledge about conditional statements, loops, lists and working with strings. I've also used the `random` built-in library to choose a random word from a list (could expand it into working with files) and the `string` library for validation (allowing only letters as input).

I've also learned that string are immutable which means that I couldn't take a character at a certain index out of the string and replace it. Instead I worked with a list of characters which I displayed by using the `.join()` method.

## Used methods
`.append()`
used it to populate the empty list with underscores and to keep track of already guessed letters

`random.randint()`
used it to choose a random word from a list of words to guess

`"".join()`
used to print a list as a string. Can define the separator, for example used ", ".join() to display the already guessed letters

`.lower()`
changed all user inputs to lowercase so it is easier to compare to the guessed word

`string.ascii_letters/ascii_lowercase` abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ
used this to make sure user entered only letters. Worked with ascii_lowercase since I already made everything into lowercase with .lower() (feels logical, semantically correct and probably gives faster results, even though it's not noticeable on a project of such small scale I assume it's good practice).

### To do:
- [ ] Refactor code, use clean code principles (especially tip 1 from this `https://www.youtube.com/watch?v=wSDyiEjhp8k` and "throw errors as fast as possible")
- [ ] Write cleaner comments
