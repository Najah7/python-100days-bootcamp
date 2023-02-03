# This lesson is for the function with argument

# Positional arguments, keyword arguments

import math
import sys


sys.path.append('../utils')
from input_helper import int_input, float_input
from output_helper import welcome

APPS = ["Cans Calc", "Prime Number Checker"]

def main():
    
    while(1):
        app = input(f'Select "{APPS[0]}", "{APPS[1]}" ')
        
        if app in APPS: break
    
    if app == APPS[0]:
        welcome('Area Calc')
        # get wall info
        height = float_input('Height of wall? ')
        width = float_input('Width of wall? ')
        # calc number of cans we will need
        num_cans = calculate_num_needed_cans(height=height, width=width)
        # print output 
        print(f"You'll need {num_cans} cans of paint")

    elif app == APPS[1]:
        welcome('Prime Number Checker')
        
        num = int_input('Input Number: ')
        
        if is_prime(num):
            print("It's a prime number")
        else:
            print("It's not a prime number")
            
        
        
def calculate_num_needed_cans(height, width):
    
    CAVERAGE_PER_CAN = 5
    
    area = height * width 
    
    num_cans = math.ceil(area / CAVERAGE_PER_CAN)
    
    return num_cans

def is_prime(num):
    
    for i in range(2, num):
        
        if num % i == 0:
            return False
        
        if i + 1 == num:
            return True
            
    



if __name__ == '__main__':
    main()