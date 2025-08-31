#For loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit) #Apple Peach Pear
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
sum_scores = 0 
for score in student_scores:
    sum_scores += score
#sum() sums all items from a list
#max() min() take max/ min item from a list 
#Challenge: Get max number from a list without max function

highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(highest_score) #199
#range(a, b, step) creates a range between 1 incluse to b not incluse with given step
for num in range(1, 11, 1):
    print(num) # 1 2 3 4 5 6 7 8 9 10 
#Challenge: sum numbers between 1 and 100 inclusive 
sum_numbers = 0 

for num in range(1, 101):
    sum_numbers += num 
print(sum_numbers)
