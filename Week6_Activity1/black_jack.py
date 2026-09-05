import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    total = sum(cards)
    return(total)

def compare(user_score, computer_score):
    if user_score > 21 :
        print("\nYou lost")
    elif computer_score > 21 :
            print("\nYou Won")
    elif user_score > computer_score :
        print("\nYou won")
    elif user_score < computer_score :
        print("\nYou Lost")
    else :
        print("Draw")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    user = []
    computer = []
    print(logo)
    user.append(deal_card())
    user.append(deal_card())
    print(f"Your cards: {user}")
    computer.append(deal_card())
    print(f"Computer's first card: {computer[0]}")
    while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user.append(deal_card())
        print(f"Your cards: {user}")

        computer.append(deal_card())
        print(f"Computer's cards: {computer}")

        if (calculate_score(user) > 21) :
            break

    if(calculate_score(computer) < 21) :
        computer.append(deal_card())
        print(f"Computer's cards: {computer}")

    compare(sum(user), sum(computer))

def main():
    while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear_console()
        play_game()

if __name__ == "__main__":
    main()


