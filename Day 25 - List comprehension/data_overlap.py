def format_file_numbers(path):
    with open(file=path) as file:
        file_data = file.read().splitlines() 
        file_numbers = [int(num) for num in file_data]
    
    return file_numbers

file_1_numbers = format_file_numbers(path="./file1.txt")
file_2_numbers = format_file_numbers(path="./file2.txt")



result = [num for num in file_1_numbers if num in file_2_numbers]

print(result)
