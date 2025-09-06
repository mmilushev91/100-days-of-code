import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
game_over = False
guessed_letters = []

for position in range(word_length):
    placeholder += "_"

print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:

        if letter == guess:
            display += letter
            guessed_letters.append(letter)
        elif letter in guessed_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("You win!")
        game_over = True
