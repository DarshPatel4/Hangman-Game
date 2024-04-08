import random
import string

# List of words for the game
words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple", "kiwi", "peach", "mango", "lemon", "cherry", "blueberry", "raspberry"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the hidden word with guessed letters
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# Main function
def main():
    print("Welcome to Hangman!")
    word = choose_word()
    print("The word has", len(word), "letters.")
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(word, guessed_letters)
        print("Word:", displayed_word)
        print("Guessed letters:", ', '.join(guessed_letters))

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess! Try again.")

        if attempts == 0:
            print("Out of attempts! The word was:", word)
            break

# Call the main function
if __name__ == "__main__":
    main()
