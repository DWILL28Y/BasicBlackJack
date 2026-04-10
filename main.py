import art
import random

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card1 = random.choice(cards)
user_card2 = random.choice(cards)
user_score = user_card1 + user_card2
computer_card1 = random.choice(cards)

print(f"Your cards are: [{user_card1},{user_card2}], current score: {user_score}")
print(f"Computers first card: {computer_card1}")
input("Press 'y' to get another card or 'n' to pass: ")

