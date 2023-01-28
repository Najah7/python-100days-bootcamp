# This lesson is for Data Types

# NOTE:Type Errorを面白い例えをしていた。
# 「ポテト入れたら、フレンチフライを出すマシンに石入れたら壊れるよね」という例え

# Stirng
# first letter
print('Hello'[0])
print('Hello'[-5])

# last letter
print('Hello'[4])
print('Hello'[-1])

# cobine strings
print('123' + '456')

# Integer
print(123 + 456)

# code styel for Integer 
# NOTE:人間が読みやすいようにアンダーバー使える。実行されるときは無視される。
print(123_456_789)

# Float
print(3.14)

# Boolean
print(True)
print(False)

# How to check type
num = 1
print(type(num))

# type changer
string_num = str(num)
int_num = int(string_num)
float_num = float(string_num)
print(type(string_num))
print(type(int_num))
print(type(float_num))

# Mathematical Operations
# NOTE: 
# How to memorize: "PEMDASLR"
# 1.Parentheses: ()
# 2.Exponents: **
# 3.Multiplication: *
# 3.Division:/
# 4.Addition: +
# 4.Subtraction: -
# Left
# Right

print(3 * 3 + 3 / 3 - 3)

print(round(8 / 3, 2))
print(8 // 3)

# short hand
total = 0
total += 2
total -=1
print(total)
total *= 4
total /= 2
print(total)

# f-string
print(f'This is {total}')

# BMI mass index
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height **2) 
print(int(bmi))

# visualize your life in weeks
age = int(input('What is your current age?: '))

MAX_AGE = 90

life_remaining = MAX_AGE - age

days_remaining = life_remaining * 365

weeks_remaining = days_remaining / 7

months_remaining = weeks_remaining / 4

message = f'You have {days_remaining} days, {int(weeks_remaining)} weeks, and {int(months_remaining)} months left.'

print(message)
