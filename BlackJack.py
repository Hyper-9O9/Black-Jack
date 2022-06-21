# A simple black jack game
# In this version when a card is drawn it will not be discarded from the deck
# Ace can count as 1 or 11
# Jack/Queen/King count as 10
# Each card has an equal probability of drawing
import os

from logo import logo
import random

def draw():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def count_score(hand):
    score = 0
    for card in hand:
        score += card
    return score



def play():
    player_hand = []
    computer_hand = []

    # initializing the hands
    for _ in range(2):
        player_hand.append(draw())
    computer_hand.append(draw())

    while True:
        print(logo)
        player_score = count_score(player_hand)
        computer_score = count_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score} \nComputer's first card: {computer_hand[0]}")

        player_input = input("Type 'y' to draw a card, type 'n' to pass: ").lower()
        if player_input == "y":
            player_hand.append(draw())
            os.system('cls')
        else:
            break


play()
