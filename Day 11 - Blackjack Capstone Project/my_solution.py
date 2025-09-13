from random import choice
from art import logo

def generate_random_cards(cards, number):
    random_cards = []
    for _ in range(number):
        random_cards.append(choice(cards))
    return random_cards

def calculate_score(cards):
    """Calculates the total score of array of scares. If score >
    21 and 11 is the last card it changes it to 1 and recalculates the
    score"""
    score = sum(cards)

    if score > 21 and cards[-1] == 11:
        cards[-1] = 1
        score -= 10

    return score

def display_current_stats(p_cards, c_hand, p_score):
    computer_first_card = c_hand[0]
    print(f"Your cards: {p_cards}, current score: {p_score}")
    print(f"Computer's first card: {computer_first_card}")

def display_final_stats(p_cards, c_hand, p_score, c_score):
    print(f"Your final hand: {p_cards}, final score: {p_score}")
    print(f"Computer's final hand: {c_hand}, final score: {c_score}")

def compare(c_score, c_cards, p_score):
    """Compare results and prints the final outcome"""
    if c_score > 21:
        print("Opponent went over. You win 😁")
    elif c_score == p_score:
        print("Draw 🙃")
    elif c_score == 21 and len(c_cards) == 2:
        print("Your Opponent has a Blackjack 😱 You lose 😤")
    elif c_score > p_score:
        print("You lose 😤")
    else:
        print("You win 😁")

def blackjack():
    while True:
        print(logo)
        game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if game_on != "y":
            break

        all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_cards = generate_random_cards(cards=all_cards, number=2)
        computer_cards = generate_random_cards(cards=all_cards, number=1)

        player_score = calculate_score(cards=player_cards)
        computer_score = calculate_score(cards=computer_cards)

        display_current_stats(p_cards=player_cards, c_hand=computer_cards, p_score=player_score)

        if player_score == 21:
            print("Win with a Blackjack 😎")
            continue
        elif player_score > 21:
            print("You went over. You lose 😭")
            continue

        while input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            player_cards.extend(generate_random_cards(all_cards, number=1))
            player_score = calculate_score(player_cards)

            display_current_stats(p_cards=player_cards, c_hand=computer_cards, p_score=player_score)

            if player_score > 21:
                display_final_stats(p_cards=player_cards, c_hand=computer_cards, p_score=player_score, c_score=computer_score)
                print("You went over. You lose 😭")
                break

        if player_score > 21:
            continue

        while computer_score < 17:
            computer_cards.extend(generate_random_cards(cards=all_cards, number=1))
            computer_score = calculate_score(cards=computer_cards)

        display_final_stats(p_cards=player_cards, c_hand=computer_cards, p_score=player_score, c_score=computer_score)
        compare(c_score=computer_score, c_cards=computer_cards, p_score=player_score)

blackjack()
