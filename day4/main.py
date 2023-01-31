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
judge = ['DRAW!', 'YOU LOSE 😞', 'YOU WIN 🎉']

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
    # 基本のplayerが勝つパターン
    if computer < player:
        pirnt('YOU WIN')
    # 勝つパターンの例外
    elif player == 2 and computer == 0:
        print('YOU LOSE')
    # 基本のplayerが負けるパターン
    elif player < computer:
        print('YOU LOSE!')
    # 負けるパターンの例外
    elif player == 0 and computer == 2:
        print('YOU WIN!')
    # 引き分け
    elif player == computer:
        print('DRAW!')
    
    '''
    
    
    
    
    


if __name__ == '__main__':
    main()