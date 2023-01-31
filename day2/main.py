# Project Tip Calculator

# 仮想環境使ってないので、わざとこの記述をしている。
import sys
sys.path.append('../utils')
from input_helper import int_input, float_input

# options wihich is percentages of tip
PERCENTAGES = [10, 12, 15]

def main():
    print('Welcome to the tip calculator.')
    
    total = float_input("What was the total bill? ")
    
    percentage = percentage_input("What percentage tip would you like to give? 10, 12, or 15? ")

    num_people = int_input("How many people to split the bill? ")

    total_with_tip = total + total * percentage 
    
    each_person_total = total_with_tip / num_people
    
    print(f'Each person should pay: {each_person_total:.2f}')

            
def is_in_options(percentage):
    if percentage in PERCENTAGES: return True
    print('You only can select a percentage in 10, 12, 15')
    return False

def to_parcentage(num):
    if not isinstance(num, int): return None
    return num / 100
  
def percentage_input(message):
    percentage = None
    while (not percentage):
        user_input = int_input(message)
        # HACK:名前
        is_ok = is_in_options(user_input)
        if is_ok:
            percentage = to_parcentage(user_input)
            return percentage
        else: 
            print(f'select a num in {PERCENTAGES[0]}, {PERCENTAGES[1]}, {PERCENTAGES[2]}')
        
    

if __name__ == '__main__':
    main()