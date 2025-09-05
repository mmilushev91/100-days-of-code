import random
import hangman_images
import hangman_words

random_word = random.choice(hangman_words.word_list)
game_lives = 6
random_word_len = len(random_word)

display_word = ["_"] * random_word_len

print(hangman_images.logo)

while game_lives > 0:
    print(f"Word to guess: {''.join(display_word)}")
    guess = input("Guess a letter: ").lower()
    letter_in_word = False

    for i in range(random_word_len):

        if random_word[i] == guess:
            display_word[i] = guess
            letter_in_word = True

    if letter_in_word:
        print(''.join(display_word))

        if not "_" in display_word:
            print(f"****************************YOU WIN! THE WORD WAS {random_word}****************************")
            break
    else:
        game_lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(hangman_images.stages[game_lives])
    print(f"****************************{game_lives}/6 LIVES LEFT****************************")
else:
    print(f"***********************IT WAS {random_word}! YOU LOSE**********************")
