import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_score = 0
computer_score = 0

def get_cards ():
    return random.choice(cards)

def current_game(current_cards, current_score, current_computer_cards):
    print(f"Your cards are: {current_cards}, current hand: {current_score}")
    print(f"Dealers first card: {current_computer_cards}")

def game_over (current_cards, current_score, current_computer_cards, current_computer_score):
    print(f"Your final cards are: {current_cards}, final hand: {current_score}")
    print(f"Dealers final cards: {current_computer_cards}, final hand: {current_computer_score}")

def check_winner(final_user_score, final_computer_score):
    if final_user_score == final_computer_score:
        return print("The game is a draw!")
    elif final_user_score > final_computer_score:
        return print("You win!")
    elif final_computer_score > 21:
        return print("Dealer bust, You win!")
    elif final_computer_score > final_user_score:
        return print("You Lose!")

blackjack = True
while blackjack:
    #reset both card lists and user/computer loops
    user_cards = []
    computer_cards = []
    user_continues = True
    computer_continues = True

    #get initial cards and setup game
    user_cards.append(get_cards())
    user_cards.append(get_cards())
    computer_cards.append(get_cards())
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    current_game(current_cards=user_cards, current_score=user_score, current_computer_cards=computer_cards)

    #if user wants another card, this starts the user loop to keep getting cards
    get_new_card = input("Press 'y' to get another card or 'n' to pass: ").lower()
    if get_new_card == 'y':
        while user_continues:
            new_card = user_cards.append(get_cards())
            user_score = sum(user_cards)

            #if the user has an Ace(11), and they are over 21, replace with #1
            while user_score > 21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                user_score = sum(user_cards)
            current_game(current_cards=user_cards, current_score=user_score, current_computer_cards=computer_cards)


            if user_score > 21:
                print("You bust, dealer wins!")
                user_continues = False
                computer_continues = False
                continue

            get_new_card = input("Press 'y' to get another card or 'n' to pass: ").lower()
            if get_new_card == 'n':
                user_continues = False

    #Computer loop, so it can get more cards
    while computer_continues:
        new_computer_card = computer_cards.append(get_cards())
        computer_score = sum(computer_cards)
        # if the computer has an Ace(11), and they are over 21, replace with #1
        while computer_score > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computer_score = sum(computer_cards)

        if computer_score <= 16:
            computer_continues = True
        else:
            computer_continues = False
            game_over(current_cards = user_cards, current_score=user_score, current_computer_cards=computer_cards, current_computer_score=computer_score)
            check_winner(final_user_score = user_score, final_computer_score = computer_score)

    #user decides if they want to play another game of not
    continue_game = input("Press 'y' to play a game of Blackjack or 'n' to quit: ").lower()
    if continue_game == 'n':
        blackjack = False
    else:
        print("\n" * 20)



