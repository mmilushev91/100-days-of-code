from menu import MENU

def print_report(resources, money):
    for resource in resources:
        line = f"{resource.title()}: {resources[resource]}"
        unit = "g" if resource == "coffee" else "ml"
        print(line + unit)
        
    print(f"Money: ${money["value"]}")

def are_resources_enough(drink, resources):
    enough_resources = True
    
    for ingredient in drink["ingredients"]:
        resource = drink["ingredients"][ingredient]
            
        if resource > resources[ingredient]:
            
            print(f"Sorry there is not enough {ingredient}.")
            enough_resources = False
    
    if enough_resources:
        return True
    
    return False
    
def validate_coin_amount(coin_name):
    coin = input(f"How many {coin_name}? ")
    
    while not coin.isnumeric():
        print("Ivalid coin amount!")
        coin = input(f"How many {coin_name}? ")
    
    return int(coin)
    
def deduct_resources(drink, resources):
    for ingredient in drink["ingredients"]:
        resource = drink["ingredients"][ingredient]
        resources[ingredient] -= resource

def coffee_machine():
    machine_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    
    machine_money = {
        "value": 0,
    }
    
    machine_on = True
    
    while machine_on:
        action = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if action == "off":
            machine_on = False
            continue
        
        if action == "report":
            print_report(resources=machine_resources, money=machine_money)
    
        elif action in ["espresso", "latte", "cappuccino"]:
            choicen_drink = MENU[action]
           
            if are_resources_enough(drink=choicen_drink, resources=machine_resources):
                
                quaters = validate_coin_amount("quaters")
                dimes = validate_coin_amount("dimes")
                nickles = validate_coin_amount("nickles")
                pennies = validate_coin_amount("pennies")
                
                paid = quaters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                cost = choicen_drink["cost"]
                
                if paid < cost:
                    print("Sorry that's not enough money. Money refunded.")
                    continue
                
                deduct_resources(drink=choicen_drink, resources=machine_resources)
                change = 0
                
                if paid > cost:
                    change = paid - cost
                    print(f"Here is ${change:.2f} dollars in change.")
                
                machine_money["value"] += cost
                print(f"Here is your {action}. Enjoy!")
         
        else:
            print("Invalid action!")

coffee_machine()
