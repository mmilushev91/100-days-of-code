def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    
    combined_name = name1.upper() + name2.upper()
    
    for letter in combined_name:
        
        if letter in "TRUE":
            true_score += 1 
        
        if letter in "LOVE":
            love_score += 1 
    
    print(f"{true_score}{love_score}")
    
    
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Marian", "Monika")
    
