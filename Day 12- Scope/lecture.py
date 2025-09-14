#Scope

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies() #enemies inside function: 2
print(f"enemies outside function: {enemies}") #enemies inside function: 1

#Local scope - Variables (or functions) 
#declared inside functions have local scope (also called function scope). 
#They are only seen by other code within the same block of code.
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion() # 2 
# print(potion_strength) #name error

#Global score - Variables or functions declared at the top level
# (unindented) of a code file have global scope. It is accessible anywhere in the code file.

player_health = 10

def drink_potion_2():
    potion_strength = 2 
    print(player_health)
#player_health is accessible inside functions because it is declared in the global scope  
drink_potion_2() # 10
