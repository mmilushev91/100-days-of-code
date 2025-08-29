print("Welcome to the tip calculator!")
 
bill = int(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

tip_amount = tip_percent / 100 * bill
bill_plus_tip = bill + tip_amount
amount_per_person = bill_plus_tip / people_count

print(f"Each person should pay: ${round(amount_per_person, 2)}")
