from random import randint

def return_attemps_count():
    mode_attempts = {
        "easy": 10,
        "hard": 5,
    }
    
    mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    while mode not in mode_attempts:
        print("Invalid mode!")
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    return mode_attempts[mode]

def return_guess_number():
    guess = input("Make a guess: ")
    
    while not guess.isnumeric():
        print("Invalid number!")
        guess = input("Make a guess: ")
    
    return int(guess)
    
def number_guessing_game():
    logo = """
 _   _                 _                                              
 _   _                 _                 
| \ | |_   _ _ __ ___ | |__   ___ _ __   
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|  
| |\  | |_| | | | | | | |_) |  __/ |     
|_|_\_|\__,_|_| |_| |_|_.__/ \___|_|     
 / ___|_   _  ___  ___ ___(_)_ __   __ _ 
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` |
| |_| | |_| |  __/\__ \__ \ | | | | (_| |
 \____|\__,_|\___||___/___/_|_| |_|\__, |
 / ___| __ _ _ __ ___   ___        |___/ 
| |  _ / _` | '_ ` _ \ / _ \             
| |_| | (_| | | | | | |  __/             
 \____|\__,_|_| |_| |_|\___|
"""
    random_number = randint(1, 100)
    
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts_count = return_attemps_count()
    
    print(f"You have {attempts_count} attempts remaining to guess the number.")
    
    while attempts_count > 0:
        guess_number = return_guess_number()
        
        if guess_number == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        
        attempts_count -= 1
        
        if attempts_count == 0:
            continue
        
        if guess_number > random_number:
            print("Too High")
        else:
            print("Too Low")
        
        print("Guess again.")
        print(f"You have {attempts_count} attempts remaining to guess the number.")
    else:
        print(f"You've run out of guesses. Start new game.")
        
number_guessing_game()
