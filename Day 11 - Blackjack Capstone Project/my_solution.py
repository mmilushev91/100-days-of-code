from random import choice

def generate_random_cards(cards, number):
    random_cards = []
    
    for _ in range(number):
        random_cards.append(choice(cards))
    
    return random_cards

def calculate_score(cards):
    return sum(cards)

def display_current_stats(cards, computer_hand, score):
    computer_first_card = computer_hand[0]
    
    print(f"Your cards: {cards}, current score: {score}")
    print(f"Computer's first card: {computer_first_card}")

def display_final_stats(p_cards, computer_hand, p_score, c_score):
    print(f"Your final hand: {p_cards}, final score: {p_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {c_score}")
    
def blackjack():
    
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    
    print("Welcome to Blackjack Game!")
    
    game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
    if game_on == "y":
    
        player_cards.extend(generate_random_cards(cards=all_cards, number=2))
        computer_cards.extend(generate_random_cards(cards=all_cards, number=1))
        player_score = calculate_score(player_cards)
        display_current_stats(player_cards, computer_cards, player_score)
        
        if player_score == 21:
            print("Win with a Blackjack 😎")
            blackjack()
        elif player_score == 22:
            print("You went over. You lose 😭")
            blackjack()
            
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        went_over = False
        
        while another_card == "y":
            player_cards.extend(generate_random_cards(cards=all_cards, number= 1))
            player_score = calculate_score(player_cards)
            
            if player_score > 21:
                if player_cards[-1] == 11:
                    player_cards[-1] = 1 
                    player_score = calculate_score(player_cards)
                else:
                    went_over = True
            
            display_current_stats(player_cards, computer_cards, player_score)
            
            if went_over:
                computer_score = calculate_score(computer_cards)
                display_final_stats(player_cards, computer_cards, player_score, computer_score)
                print("You went over. You lose 😭")
                blackjack()
            
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        went_over = False
        
        while computer_score < 17:
            computer_cards.extend(generate_random_cards(computer_cards, 1))
            computer_score = calculate_score(computer_cards)
            
            if computer_score > 21:
                if computer_cards[-1] == 11:
                    computer_cards[-1] = 1 
                    computer_score = calculate_score(computer_cards)
                else:
                    went_over = True
                
            if went_over:
                display_final_stats(player_cards, computer_cards, player_score, computer_score)
                print("Opponent went over. You win 😁")
                blackjack()
        
        display_final_stats(player_cards, computer_cards, player_score, computer_score)
        
        if computer_score == player_score:
            print("Draw 🙃")
            blackjack()
        elif computer_score > player_score:
            
            if computer_score == 21 and len(computer_cards) == 2:
                print("Your Opponent has a Blackjack")
            print("You lose 😤")
            blackjack()
            
        else:
            print("You win 😁")
            blackjack()

blackjack()
        
    




