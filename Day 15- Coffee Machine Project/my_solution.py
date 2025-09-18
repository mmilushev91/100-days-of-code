from menu import MENU

def print_report(resources, money):
    for resource in resources:
        line = f"{resource.title()}: {resources[resource]}"
        unit = "g" if resource == "coffee" else "ml"
        print(line + unit)
        
    print(f"Money: ${money["value"]}")

def are_resources_enough(drink, resources):
    
    for ingredient in drink["ingredients"]:
        resource = drink["ingredients"][ingredient]
            
        if resource > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def validate_coin_amount(coin_name):
    coin = input(f"How many {coin_name}? ")
    
    while not coin.isnumeric():
        print("Ivalid coin amount!")
        coin = input(f"How many {coin_name}? ")
    
    return int(coin)

def calculate_paid():
    print("Please insert coins: ")
    paid = validate_coin_amount("quaters") * 0.25
    paid += validate_coin_amount("dimes") * 0.10
    paid += validate_coin_amount("nickles") * 0.05
    paid += validate_coin_amount("pennies") * 0.01

    return paid
    
def deduct_resources(drink, resources):
    for ingredient in drink["ingredients"]:
        resource = drink["ingredients"][ingredient]
        resources[ingredient] -= resource

def is_order_completed(drink, resources, money, act):
    
    if are_resources_enough(drink, resources):
        paid = calculate_paid()       
        cost = drink["cost"]
                
        if paid < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
                    
        deduct_resources(drink, resources)
        change = 0
                    
        if paid > cost:
            change = paid - cost
            print(f"Here is ${change:.2f} dollars in change.")
            
        money["value"] += cost
        print(f"Here is your {act}. Enjoy!")
        return True
    
    return False
        

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
            
        elif action == "report":
            print_report(resources=machine_resources, money=machine_money) 
            
        elif action in ["espresso", "latte", "cappuccino"]:
            choicen_drink = MENU[action]
            is_order_completed(drink=choicen_drink, resources=machine_resources, money=machine_money, act=action)
        else:
            print("Invalid action!")

coffee_machine()
