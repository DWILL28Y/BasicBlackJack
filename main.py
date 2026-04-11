import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

def get_cards ():
    return random.choice(cards)

def current_game(current_cards, current_score, current_computer_cards):
    print(f"Your cards are: {current_cards}, current hand: {current_score}")
    print(f"Computers first card: {current_computer_cards}")

def game_over (current_cards, current_score, current_computer_cards, current_computer_score):
    print(f"Your final cards are: {current_cards}, final hand: {current_score}")
    print(f"Computers final cards: {current_computer_cards}, final hand: {current_computer_score}")

user_continues = True
computer_continues = True
blackjack = True
while blackjack:
    user_cards.append(get_cards())
    user_cards.append(get_cards())
    computer_cards.append(get_cards())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    current_game(current_cards=user_cards, current_score=user_score, current_computer_cards=computer_cards)
    get_new_card = input("Press 'y' to get another card or 'n' to pass: ")
    if get_new_card == 'y':
        while user_continues:
            new_card = user_cards.append(get_cards())
            user_score = sum(user_cards)
            current_game(current_cards=user_cards, current_score=user_score, current_computer_cards=computer_cards)
            get_new_card = input("Press 'y' to get another card or 'n' to pass: ")
            if get_new_card == 'n':
                user_continues = False
            else:
                user_continues = True


    while computer_continues:
        new_computer_card = computer_cards.append(get_cards())
        computer_score = sum(computer_cards)
        if computer_score <= 16:
            computer_continues = True
        else:
            computer_continues = False
            game_over(current_cards = user_cards, current_score=user_score, current_computer_cards=computer_cards, current_computer_score=computer_score)
    print("\n" * 20)


