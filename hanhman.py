import random

def hangman_game():
    words = ["algorithm", "function", "variable", "compile", "iterate", "recursion", "binary", "array", "syntax", "pointer"]
    max_incorrect_attempts = 7  # Matches the number of letters in "HANGMAN"
    
    while True:
        word = random.choice(words)
        guessed_word = ["_"] * len(word)
        attempts_left = max_incorrect_attempts
        guessed_letters = set()
        
        print("HANGMAN")
        print("^".ljust(8))  # Pointer starts under 'H'
        
        while attempts_left > 0:
            print("\n", " ".join(guessed_word))  # Display current word progress
            guess = input("Guess a letter: ").lower()
            
            # Validate input
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetic character.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter. Try another one.")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word:
                for i, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[i] = guess
                print("Good guess!")
            else:
                attempts_left -= 1
                pointer_position = " " * (8 - attempts_left) + "^"
                print("Wrong guess!")
                print("HANGMAN")
                print(pointer_position)
            
            if "_" not in guessed_word:
                print("\nCongratulations! You guessed the word: '{}'".format(word))
                print("Phew... you are saved")
                break
        else:
            print("\nYou are hanged!")
            print("The word was:", word)
        
        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thank you for playing Hangman!")
            break

if __name__ == "__main__":
    hangman_game()
