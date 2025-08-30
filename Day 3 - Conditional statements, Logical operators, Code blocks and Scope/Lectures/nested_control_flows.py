#Nested conditionals and elif. Multiple if-s
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can get on the rollercoaster!")
    
    age = int(input("What is your age? "))
    price = 0
    
    if age <= 12:
        price = 5
        print("Child ticket is $5.")
    elif age <= 18:
        price = 7
        print("Youth ticket is $7")
    else:
        price = 12 
        print("Adult ticket is $12")
    
    want_photo = input("Do you want a photo (yes/no)? ")
    
    if want_photo == "yes":
        price += 3
        
    print(f"Final price is: ${price}")
else:
    print("You have to grow up to use the rollercoaster!")
