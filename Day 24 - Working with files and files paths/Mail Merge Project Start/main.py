#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.as
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def split_file_content(file_path):
    with open(file=file_path, mode="r") as file:
         file_content_list = file.read().split("\n")

    return file_content_list

letter_sentences = split_file_content(file_path="./Input/Letters/starting_letter.txt")
invited_names_list = split_file_content(file_path="./Input/Names/invited_names.txt")

for name in invited_names_list:
    greeting = f"Dear {name},"
    letter_sentences[0] = greeting
    new_letter_text = "\n".join(letter_sentences)

    with open(file=f"./Output/ReadyToSend/{name}.txt", mode="w") as letter_text:
        letter_text.write(new_letter_text)


