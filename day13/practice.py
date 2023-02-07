# This lesson is for the Debugging

# Everyone gets bugs

# Tips to fix a bug
# 1. Describe the Problem
# 2. Reproduce the Bug
# 3. play Computer and Evaluate Each line
# 4. Fix the Errors and Watching for Red Underlines
# 5. print is your Friend NOTE:if you had heartbreak, use print :)（面白かった）
# 6. use Debbuger (Sony, Python Tutorなど) NOTE:Bring out the BIG Gun
# 7. Take a Break
# 8. Ask a Friend
# 9. Run Often
# 10. Ask StackOverflow(最終手段)

############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])