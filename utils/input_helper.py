
def int_input(message):
    
    while 1: 
        try:
            user_input = int(input(message))
            return user_input
        except:
            print("You should input the number")
            continue

def natural_num_input(message):
    
    while 1:
        num = int_input(message)
        # HACK: このifでOK？
        if 0 <= num and not isinstance(num, float):
            return num
        else: 
            print('you should input natural number')
            continue
            


def float_input(message):

    while 1:
        try:
            num = float(input(message))
            return num
        except: 
            print("You should input the number")
            continue

    
   
def yes_no_input(message):
    
    while(1):
            user_input = input(message)
            # handle starting with "y" is "yes" and "n" is "no"
            if user_input[0].upper() == 'Y': return True
            elif user_input[0].upper() == 'N': return False
            else: print("Sorry, I can't understand yor answer.")