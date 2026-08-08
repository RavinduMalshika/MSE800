import random
import string

class Game:
    # List of words
    words = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]

    # Initilaize the class
    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.lives = max_lives
        self.secret_word = random.choice(self.words)
        self.blanks = ["_" for _ in self.secret_word]
        self.used_letters = set()

    def prompt_for_letter(self, used_letters):

        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in used_letters:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, word, blanks, letter):

        found_any = False
        for i, ch in enumerate(word):
            if ch == letter and blanks[i] == "_":
                blanks[i] = letter
                found_any = True
        return found_any

    def all_blanks_filled(self, blanks):
    
        return "_" not in blanks

    def play_game(self):
        
        secret = self.secret_word
        blanks = self.blanks
        lives = self.max_lives
        used = self.used_letters

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(secret)} letters.")
        print(" ".join(blanks))

        while True:
            # Ask the user to guess a letter
            guess = self.prompt_for_letter(used)
            used.add(guess)

            # Is the guessed letter in the word?
            if self.reveal_letters(secret, blanks, guess):
                print("\n Well done, Nice job! You found a letter.")
                print(" ".join(blanks))
                # Are all blanks filled?
                if self.all_blanks_filled(blanks):
                    print("\n Congratulation! You guessed the word!")
                    print(f"Word: {secret}")
                    print("GAME OVER")
                    break
            else:
                # Lose a life
                lives -= 1
                print(f"\nNope. You lose a life. Lives left: {lives}")
                print(" ".join(blanks))

                # Have they run out of lives?
                if lives <= 0:
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {secret}")
                    print("GAME OVER")
                    break

            # (loop continues to ask for another letter)

def main():
    game = Game()       #Create object of Game
    game.play_game()    #Call the play_game method

if __name__ == "__main__":
    main()
