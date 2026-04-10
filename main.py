import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0

def get_user_cards ():
    user_new_card = random.choice(cards)
    return user_new_card

def get_computer_cards ():
    computer_new_card = random.choice(cards)
    return computer_new_card

def current_game(current_cards, current_score, computer_cards):
    print(f"Your cards are: {current_cards}, current hand: {current_score}")
    print(f"Computers first card: {computer_cards}")

blackjack = True
while blackjack:
    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    computer_card1 = random.choice(cards)
    user_score += user_card1 + user_card2
    computer_cards = [user_card1]
    user_cards = [user_card1, user_card2]
    current_game(current_cards=user_cards, current_score=user_score, computer_cards=computer_cards)
    get_new_card = input("Press 'y' to get another card or 'n' to pass: ")

    if get_new_card == 'y':
        user_card3 = get_user_cards()
        user_cards.append(user_card3)
        current_game(current_cards=user_cards, current_score=user_score, computer_cards=computer_cards)

    else:
        computer_card2 = get_computer_cards()
        computer_cards.append(computer_card2)
        