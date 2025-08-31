import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
last_letters_index = len(letters) - 1
last_symbols_index = len(symbols) - 1
last_numbers_index = len(numbers) - 1


for letter in range(nr_letters):
    random_index = random.randint(0, last_letters_index)
    password += letters[random_index]

for letter in range(nr_symbols):
    random_index = random.randint(0, last_symbols_index)
    password += symbols[random_index]

for letter in range(nr_numbers):
    random_index = random.randint(0, last_numbers_index)
    password += numbers[random_index]

print(f"Your password is: {password}")
