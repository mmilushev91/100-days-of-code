from random import choice
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def calculate_score(cards):
    """Returns 0 if blackjack is scored.
       Return the sum of an array of cards. Replace
       last ace with one if score is over 21
    """
    score = sum(cards)

    if len(cards) == 2 and score == 21:
        return 0

    if score > 21 and cards[-1] == 11:
        cards[-1] = 1
        score -= 10

    return score

def compare(u_score, c_score):
    if u_score == c_score:
        print("Draw")
    elif computer_score == 0:
        print("Your Opponent has a blackjack. You lose")
    elif u_score == 0:
        print("Blackjack. You win")
    elif u_score > 21:
        print("You went over. You lose")
    elif computer_score > 21:
        print("Your Opponent went over. You win")
    elif u_score > computer_score:
        print("You win.")
    else:
        print("You lose")


play_blackjack = input("Do want to play blackjack 'y' or 'n': ")

while play_blackjack == "y":
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1
    is_game_on = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(logo)
    while is_game_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}. current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or \
            user_score > 21:
            is_game_on = False
        else:
            another_card = input("Type 'y' to get another card or 'n' to pass: ")

            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_on = False

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}. final score: {user_score}")
    print(f"Computer final hand: {computer_cards}. final score: {computer_score}")
    compare(user_score, computer_score)

    play_blackjack = input("Do want to play blackjack 'y' or 'n': ")
