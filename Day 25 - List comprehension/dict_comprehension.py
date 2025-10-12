from random import randint
# Dictionary comprehension
# new_dic = {new_key: new_value for item in list ]
# new_dic = {new_key: new_value for (key, value) in dic.items() ]
# new_dic = {new_key: new_value for (key, value) in dic.items() if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name:randint(1, 100) for name in names}
print(student_scores)
passed_students = {name:score for (name, score) in student_scores.items() if score >= 60}
print(passed_students)
