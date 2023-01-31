# This Lecture for the Loop.

# NOTE:Web site to check your address pwnde.(https://haveibeenpwned.com/)

# NOTE:List of the most common passwords(https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)


# function list of which appear in this lecture
# sum()
# max()
# range()

import sys
sys.path.append('../utils')
from input_helper import int_input, float_input
from output_helper import welcome

APPS = ["Calculate Average", "Find Highest", "Fizz Buzz"]

def main():
    
    while(1):
        app = input(f'Select "{APPS[0]}", "{APPS[1]}", "{APPS[2]}" ')
        
        if app in APPS: break
    
    #   Calculate Average
    if app == APPS[0]:
        
        welcome(APPS[0])
        
        heights = list()
        
        while(1):
            user_input = float_input('Input number. Enter "0" to calculate average: ')
            
            if user_input == 0: break
            else: heights.append(user_input)
        
        cal = Calculator(heights)
        
        print(cal.average())
    
    # Find Highest
    elif app == APPS[1]:
        welcome(APPS[1])
        
        nums = list()
        
        while(1):
            user_input = int_input('Input integer number. Enter "0" to find highest: ')
            
            if user_input == 0: break
            else: nums.append(user_input)
        
        cal = Calculator(nums)
        print(cal.find_highest())
    
    # Fizz Buzz
    elif app == APPS[2]:
        
        welcome(APPS[2])
        
        max = int_input('Input max number.')
        
        fizz_buzz = FizzBuzz(max)
        fizz_buzz.print()
        

class Calculator:
    def __init__(self, nums) -> None:
        self._nums = nums
    
    def average(self):
        
        # edition to use for statement
        # total = 0
        # for num in self._nums:
        #     total += num
        
        # edition to use sum function
        total = sum(self._nums)
        
        average = round(total / len(self._nums))
        
        return average
    
    def find_highest(self):
        
        # edition to use for statement
        # max = 0
        # for num in self._nums:
        #     if max < num:
        #         max = num
        
        # return max
        
        # edition to use max function
        return max(self._nums)
    

class FizzBuzz:
    def __init__(self, max) -> None:
        self._max = max
    
    def print(self):
        for i in range(self._max):
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)
            

if __name__ == '__main__':
    main()