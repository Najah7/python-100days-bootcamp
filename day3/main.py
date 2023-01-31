
# NOTE:ascii art web page:https://ascii.co.uk/art

def main():
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    # Round 1
    while True:
        choice1 = input('You are at crossroad, where do you want to go ?'
                        'Type "Left" or "Right" ')
        if choice1 == 'Right':
            print('Good Choice')
            break
        elif choice1 == 'Left':
            print('Game Over')
            break
        else:
            print('Wrong input')
    
    
    # Round 2
    while True:
        choice2 = input("You've come to lake." 
                        'There is island in the middle of the lake.'
                        'Type "Wait" to wait for a boat.'
                        'Type "Swim" to swim across. ')
        if  choice2 == 'Wait':
            print('Good Choice')
            break
        elif choice2 == 'Swim':
            print('Game Over')
            break
        else:
            print('Wrong input')

    # Round3
    doors = ['red', 'yello', 'blue']
    choice3 = input('You arrive at the unharmed.'
                    'There is a house with 3 doors.'
                    'One red, One yello, One blue'
                    'Which door do you choose? ')
    if choice3 == 'yello':
        print('You win!')
    elif not choice3 in doors:
        print('Wrong input')
    else: 
        print('Game Over')
    
if __name__ == '__main__':
    main()
    

