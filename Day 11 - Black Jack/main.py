import random
from art import logo
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def clear():
    """Clears screen. Assumes Linux. Use cls for Windows."""
    system('clear')


def dealerFunction(player_cards, computer_cards):
    while calculate_score(computer_cards) < 17:
        computer_cards.append(draw())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your final hand:{player_cards}, final score:{player_score}")
    print(f"Computer's final hand:{computer_cards}, final score:{computer_score}")
    if player_score == 21 and len(player_cards) == 2 and computer_score == 21 and len(player_cards) > 2:
        print("You win! Blackjack!")
    if player_score == 21 and len(player_cards) == 2 and computer_score == 21 and len(player_cards) == 2:
        print("You tie!")
    if calculate_score(player_cards) > 21:
        print("You lose!")
    elif calculate_score(computer_cards) > 21:
        print("You win!")
    elif calculate_score(computer_cards) == calculate_score(player_cards):
        print("You tie!")
    elif calculate_score(computer_cards) > calculate_score(player_cards):
        print("You lose!")
    else:
        print("You win!")
    playBlackJack()


def draw():
    return random.choice(cards)


def calculate_score(cards):
    """Input a list of integers, get back a black jack score"""
    score = sum(cards)
    if score > 21:
        while 11 in cards and score > 21:
            i = cards.index(11)
            cards[i] = 1
            score = sum(cards)
    return score


def playBlackJack():
    # Quit if not playing
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if not play == 'y':
        return

    clear()
    print(logo)

    # Setup initial table
    player_cards = []
    computer_cards = []
    # draw two cards for player
    player_cards.append(draw())
    player_cards.append(draw())
    # draw one card for computer
    computer_cards.append(draw())

    continue_game = True
    while continue_game:
        player_score = calculate_score(player_cards)

        if player_score > 21:
            dealerFunction(player_cards, computer_cards)
            continue_game = False
        else:
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Account for 21
            if player_score == 21:
                hitMe = 'n'
            else:
                hitMe = input("Type 'y' to get another card, type 'n' to pass: ")

            if hitMe == 'y':
                player_cards.append(draw())
                continue_game = True
            else:
                dealerFunction(player_cards, computer_cards)
                continue_game = False


playBlackJack()
