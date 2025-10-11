#list comprehension
# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers) # [2, 3, 4]

name = "Marian"
letter_list = [letter for letter in name]
print(letter_list) # ["M", "a", "r", "i", "a", "n"]

doubled_numbers = [num * 2 for num in range(1, 5)]
print(doubled_numbers) # [2, 4, 6, 8]

#Conditional list comprehension
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names_list = [name for name in names if len(name) < 5]
print(short_names_list)
long_names_list = [name.upper() for name in names if len(name) > 4]
print(long_names_list)
