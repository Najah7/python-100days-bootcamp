# Project BlackJack

# Aceのルールは知らなかったので実装してない。

import random
import sys

sys.path.append('../utils')
from input_helper import float_input, yes_no_input
from output_helper import welcome

from art import LOGO


CARDS = []

def main():
    
    should_continue = yes_no_input("Do you want to play a game of BlackJack? Type 'y' or 'no': ")

    while should_continue:
        
        welcome('Black Jack')
        
        print(LOGO)
        
        player_hand = generate_first_hand_list()
        computer_hand = generate_first_hand_list()
        
        print(f'Your current card: {player_hand}')
        print(f"Computer's first card: {computer_hand[0]}")
        
        while True:
            need_another_card = yes_no_input("Type 'y' to get another card, type 'n' to pass: ")
            
            if need_another_card:
                player_hand.append(generate_random_card_num())
                if is_bust(tuple(player_hand)): break
            else: break   
            
        player_final_score = sum(player_hand)
        computer_final_score = sum(computer_hand)
            
        print(f"You're final hand: {player_hand}, final score: {player_final_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_final_score}")
        
        if 21 < player_final_score:
            print('You wnet over. You lose🥲')
        elif computer_final_score < player_final_score:
            print('You win 🎉')
        elif computer_final_score == player_final_score:
            print('Draw!!')
        else:
            print("You lose 🥲")
            
        should_continue = yes_no_input('Do you want to play again? ')
    
    print('Bye')
            
            
        
# HACK:名前
def generate_random_card_num():
    random_num = random.randint(1, 13)
    # ブラックジャックのルールに起因したした分岐
    if 11 <= random_num <= 13:
        return 10
    elif random_num == 1:
        return 11       
    else:
        return random_num

# HACK:名前
def generate_first_hand_list():
    return [generate_random_card_num(), generate_random_card_num()]
    
    
def is_bust(hand):
    if 21 < sum(hand): return True
    return False
        
        
if __name__ == '__main__':
    main()