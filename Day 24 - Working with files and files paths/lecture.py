#Pytthon open file
file = open(file="my_file.txt", mode="r")
#Python read file and save the content to a variable
file_content = file.read()
print(file_content)

#Python close file that is already opened
file.close()

#same functionality as above but with a with statement, but this will automatically close the file
with open(file="my_file.txt", mode="r") as file:
    file_content = file.read() 
    print(file_content)

#Python write to file we need to change the mode to write, since by default it is read only
#write mode will overwrite the content of the file
#if fule does not exist it will create a new file
with open(file="my_file.txt", mode="w") as file:
    file.write("\nStudy to become a Python Developer")

#add content to file without overwriting the content
with open(file="my_file.txt", mode="a") as file:
  file.append("\nSecond line")
    
