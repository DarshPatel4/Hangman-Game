import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple"]

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
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts left:", attempts)
        displayed_word = display_word(word, guessed_letters)
        print("Word:", displayed_word)

        if "_" not in displayed_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")

        if attempts == 0:
            print("Out of attempts! The word was:", word)
            break

# Call the main function
if __name__ == "__main__":
    main()


# import time

# def calculate_typing_speed(text, elapsed_time):
#     words = text.split()
#     num_words = len(words)
#     minutes = elapsed_time / 60
#     wpm = num_words / minutes
#     return wpm

# def main():
#     print("Welcome to the Typing Speed Tester!")
#     print("Type the following text as fast as you can:")

#     # Text to be typed
#     text = "The quick brown fox jumps over the lazy dog."
#     print(text)
    
#     input("Press Enter when you are ready to start typing...")
    
#     start_time = time.time()
#     user_input = input("Start typing: ")
#     end_time = time.time()

#     elapsed_time = end_time - start_time
#     typing_speed = calculate_typing_speed(text, elapsed_time)
    
#     print("\nYou typed the text in {:.2f} seconds.".format(elapsed_time))
#     print("Your typing speed is {:.2f} words per minute (wpm).".format(typing_speed))

# if __name__ == "__main__":
#     main()
