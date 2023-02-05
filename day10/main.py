# Project Calculator

# NOTE:str().title()：単語の最初の文字を大文字に

import sys
sys.path.append('../utils')
from input_helper import float_input, yes_no_input
from output_helper import welcome

from art import LOGO

prev_amount = 0

OPERATIONS = ['+', '-', '*', '/']

def main():
    
    print(LOGO)
    
    welcome('calculate')
    
    # 最初だけ取得する値
    # get user input
    first_num = float_input("What's the first number? ")
    
    # ２回目以降の処理
    while True:
        # get user input
        operation = operation_input("Pick an operation? ")
        second_num = float_input("What's the next number? ")
        
        # calulate
        result = calculator(first_num, second_num, operation)
        
        #print result 
        print(f"{first_num} {operation} {second_num} = {result}")
        
        # keep the amount
        first_num = result
        
        # ask user to continue to calulate
        should_continue = yes_no_input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ") 
        
        if not should_continue: break
        

def add(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def multiple(num1, num2):
    return num1 * num2

def calculator(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtraction(num1, num2)
    elif operation == '*':
        return multiple(num1, num2)
    elif operation == '/':
        return division(num1, num2)
    else:
        return False

def is_opration(operation):
    while True:
        if operation in OPERATIONS:
            return True
        else:
            return False

def operation_input(message):
    
    error_msg = "You should pick up a operation in '+', '-', '*' and '/'"
    
    while True:
        operation = input(message)
        
        if is_opration(operation):
            break
        else:
            print(error_msg)
    
    return operation
    

if __name__ == '__main__':
    main()

