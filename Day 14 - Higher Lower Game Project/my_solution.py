from random import choice
from data import game_data
from art import game_logo, vs_logo

def generate_random_celebrities(data):
   
    first = choice(game_data)
    second = choice(game_data)
    
    while first == second:
        second = choice(game_data)
    
    return [first, second]

def display_celebrities(a, b, logo):
    
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(logo)
    print(f"Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.")

def validate_answer():
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
    while answer != "a" and answer != "b":
        print("Invalid input!")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    return answer

def is_correct(a, b, answer):
            
    if (answer == "a" and a["follower_count"] > b["follower_count"])\
        or (answer == "b" and a["follower_count"] < b["follower_count"]):
        return True
    else:
        return False
    
    
def game():
    
    game_on = True
    score = 0
    
    print(game_logo)
    
    while game_on:
        choice_a, choice_b = generate_random_celebrities(game_data)
        display_celebrities(choice_a, choice_b, vs_logo)
        
        user_answer = validate_answer()
        print(user_answer)
        
        if is_correct(choice_a, choice_b, user_answer):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_on = False
            print("\n" * 20)
            print(game_logo)
            print(f"Sorry, that's wrong. Final score: {score}")
      
game()
