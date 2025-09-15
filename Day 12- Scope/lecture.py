"""Scope determines the region of the code where a particular 
namespace is accessible. It defines the visibility and lifetime of variables. 
Python follows the LEGB rule (Local, Enclosing, Global, Built-in) 
to resolve variable names:

Local scope: Names defined inside a function.

Enclosing scope: Names in the enclosing function (for nested functions).

Global scope: Names defined at the top level of a module.

Built-in scope: Names pre-defined by Python (e.g., print, len).
"""

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

"""Namespace - A namespace is essentially a mapping of names (identifiers) to objects. 
It acts like a dictionary where the keys are variable names, and the 
values are the objects they reference. For example, when you assign x = 10,
the name x is added to a namespace, pointing to the value 10. Python maintains 
different namespaces, such as the local, global, and built-in namespaces.
"""
#Block scope - python doesn't have a block scope. Blocks like for, while loops
#and if else statements don't create local scope 

game_level = 3 

if game_level < 5:
    new_enemy = "monster"
#new_enemy has now a global scope. if it was created inside a function it 
#would has a local scope. Notice that you will get warnings from the edditor
#if write code like this since if game_level >= 5 there will be no new_enemy
#and you will have name error. Good practice is to declare the variable inside
#the upper of the block scope
print(new_enemy) # monster
