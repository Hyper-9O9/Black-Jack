# A simple black jack game
# In this version when a card is drawn it will not be discarded from the deck
# Ace can count as 1 or 11
# Jack/Queen/King count as 10
# Each card has an equal probability of drawing
import os

from logo import logo
import random

def draw():
    """"adding a card to hand"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def count_score(hand):
    """"calculating the sum of cards in hand"""
    score = 0
    for card in hand:
        score += card
    return score

def compare(player_score, computer_score):
    """"comparing between player and pc hand"""
    if player_score == 21:
        print("BLACK JACK you win 😎!! ")
    elif computer_score == 21:
        print("Opponent got BLACK JACK 😱, you lose!! ")
    elif player_score == computer_score:
        print("Draw 😱, we will settle this one day!")
    elif player_score > 21:
        print("You went over the limit you lose 😱!! ")
    elif computer_score > 21:
        print("Opponent went over the limit they lose 😎!!")
    elif player_score > computer_score:
        print("You win 😎")
    else:
        print("Opponent win's 😱")



def play():
    player_hand = []
    computer_hand = []

    # initializing the hands
    for _ in range(2):
        player_hand.append(draw())
    computer_hand.append(draw())

# asking the player of the want to draw a card
    in_game = False
    while not in_game:
        print(logo)

        player_score = count_score(player_hand)
        computer_score = count_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score} \nComputer's first card: {computer_hand[0]}")

    # if player has more than 21 -> finish the game
        if player_score >21:
            in_game = True
        else:
            # if player has less than 21 ask them if the want to draw
            player_input = input("Type 'y' to draw a card, type 'n' to pass: ").lower()
            if player_input == "y":
                player_hand.append(draw())
                os.system('cls')
            else:
                in_game = True


# the computer will draw till it's score is higher than player
    while  (computer_score < player_score and not player_score > 21):
        computer_hand.append(draw())
        computer_score= count_score(computer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score} \n  Computer's final hand: {computer_hand}, final score: {computer_score}")
    compare(player_score,computer_score)


# asking user if they want to play
while input("Type 'y' to play, type 'n' to exit ").lower() == "y":
    play()
    input("Press enter to go back to main menu: ")
    os.system('cls')

print("THANKS FOR PLAYING :)")
input()
