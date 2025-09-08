from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

def validate_shift():
    shift_number = input("Type the shift number:\n")

    while not shift_number.isnumeric():
        print("Please type a positive integer number!")
        shift_number = input("Type the shift number:\n")

    return int(shift_number)

def handle_letter(letter, shift_amount, activity):
    if letter not in alphabet:
        return letter

    letter_index = alphabet.index(letter)
    if activity == "encode":
        return alphabet[(letter_index + shift_amount) % alphabet_len]
    else:
        return alphabet[(letter_index - shift_amount) % alphabet_len]

print(logo)

program_runs = True
while program_runs:
    display_text = ""

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid command. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = validate_shift()

    for char in text:
        display_text += handle_letter(char, shift, direction)

    print(f"Here's the {direction}d result: {display_text}")

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()
    if restart != "yes":
        program_runs = False
        print("Goodbye!")
