#Nested conditionals and elif

print("Welcome to the rollercoaster")
height = int(input("What is your height? "))

if height >= 120:
    print("You can get on the rollercoaster!")
    
    age = int(input("What is your age? "))
    price = 0
    
    if age <= 12:
        price = 5
    elif age <= 18:
        price = 7
    else:
        price = 12 
        
    print(f"Ticket price is: ${price}")
else:
    print("You have to grow up to use the rollercoaster!")
