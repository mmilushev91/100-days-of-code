import pandas

nato_phonetic_alphabet_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dic = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}

input_word = input("Enter a word: ")
nato_phonetic_input_word_list = [nato_phonetic_alphabet_dic[letter.upper()] for letter in input_word]
print(nato_phonetic_input_word_list)
