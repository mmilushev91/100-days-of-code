import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

df = pandas.DataFrame(student_dict)

for (index, row) in df.iterrows():
    print(index)
    print(row.student)
    print(row.score)
