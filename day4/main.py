# Project The World Rock Paper Scissors 

# NOTE:The World Rock Paper Scissors Association(https://wrpsa.com/)

import random
import time

import sys
sys.path.append('../utils')
from input_helper import int_input



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''





HANDS = [rock, scissors, paper]
judge = ['DRAW!', 'YOU LOSE ð', 'YOU WIN ð']

def main():
    # ask player's choice
    while True:
        # get input
        player = int_input('What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Papper')
        # handle error
        if 0 <= player <= 2: break
        else: print('input number in 0, 1, 2')
    
    # output user's hand
    print(HANDS[player])
    print('*** Your Hand ***')
    
    # take a pause
    time.sleep(1)
    
    # output computer's choice
    computer = random.randint(0, 2)
    print(HANDS[computer])
    print('*** Computer\'s Hand ***')
    
    # shortest edition
    judge_index = (player - computer) % 3
    print(judge[judge_index])
    
    # simple edition to understand
    '''
    # åºæ¬ã®playerãåã¤ãã¿ã¼ã³
    if computer < player:
        pirnt('YOU WIN')
    # åã¤ãã¿ã¼ã³ã®ä¾å¤
    elif player == 2 and computer == 0:
        print('YOU LOSE')
    # åºæ¬ã®playerãè² ãããã¿ã¼ã³
    elif player < computer:
        print('YOU LOSE!')
    # è² ãããã¿ã¼ã³ã®ä¾å¤
    elif player == 0 and computer == 2:
        print('YOU WIN!')
    # å¼ãåã
    elif player == computer:
        print('DRAW!')
    
    '''
    
    
    
    
    


if __name__ == '__main__':
    main()