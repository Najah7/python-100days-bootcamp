# Project Tip Calculator

# options wihich is percentages of tip
PERCENTAGES = [10, 12, 15]

def main():
    print('Welcome to the tip calculator.')
    
    total = float_input("What was the total bill? ")
    
    percentage = percentage_input("What percentage tip would you like to give? 10, 12, or 15? ")

    num_people = int_input("How many people to split the bill? ")

    total_with_tip = (total + total * percentage) / num_people

    print(f'Each person should pay: {total_with_tip:.2f}')


def float_input(message):
    retval = None

    while not retval:
        try:
            retval = float(input(message))
        except: print("You should input the number")

    return retval

def int_input(message):
    retval = None
    
    while not retval: 
        try:
            return int(input(message))
        except:
            print("You should input the number")
            
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
        # options means the constant called OPTIONS
        flg = is_in_options(user_input)
        if flg:
            percentage = to_parcentage(user_input)
            return percentage
        else: 
            print('select a num in options')
        
    

if __name__ == '__main__':
    main()