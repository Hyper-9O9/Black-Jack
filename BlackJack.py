# A simple black jack game
# In this version when a card is drawn it will not be discarded from the deck
# Ace can count as 1 or 11
# Jack/Queen/King count as 10
# Each card has an equal probability of drawing
from logo import logo
import random

print(logo)
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

user_cards = []
cpu_cards = []

def hand_initializer():
    """"Initializes the beginning of the game"""
    user_total_score = 0
    while len(user_cards) != 2:
        user_cards.append(cards[random.randint(0,len(cards)-1)])

    for position in range(0,len(user_cards)):
        user_total_score += user_cards[position]

    cpu_cards.append(cards[random.randint(0,len(cards)-1)])
    print(f"Your cards: {user_cards}, current score: {user_total_score} ")
    print(f"Computer's first card: {cpu_cards[0]}")

def start_game():
    hand_initializer()

