# This lesson is for list Comprehension(リスト内包表記) and Dictionary Comprehension（辞書内包表記）

# NOTE:内包表記はシーケンスに使える

"""
NOTE:Pyhon Sequences
・list
・range
・string
・tuple
"""

"""
List Comprehension
new_list = [new_item for item in list]
"""

numbers = [ num for num in range(1, 11) ]

doble_numbers = [ num * 2 for num in numbers ]

print(numbers)
print(doble_numbers)

name = 'tuser'
name_letters = [ letter for letter in name ]
print(name_letters)

"""
Conditional List Comprehension
new_list = [new_item for item in list if test]
"""
even_nums = [ even for even in numbers if even % 2 == 0 ]
print(even_nums)

names = ['alex', 'beth', 'caroline', 'dave']
captal_names = [ name.capitalize() for name in names]
print(captal_names)

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_nums = [ num ** 2 for num in nums]

print(squared_nums)

"""
Dictionary Comprehension
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}
"""
import random
students_scores = { name: random.randint(1,100) for name in names}
print(students_scores)

"""
Conditional Dictionary Comprehension
new_dict = {new_key:new_value for (key, value) in dict.items() if test}
"""
passed_students = { name: score for (name, score) in students_scores.items() if score >= 70}
print(passed_students)

"""
How to iterate over a pandas DataFrame
"""

students_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in students_dict.items():
    print(key, value)
    
import pandas

df_student = pandas.DataFrame(students_dict)

for (index, row) in df_student.iterrows():
    print(f'{index}\n',row.student, row.score)