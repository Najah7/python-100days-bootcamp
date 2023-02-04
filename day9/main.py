# Project First-Price Sealed-bid Auction

import sys
sys.path.append('../utils')
from input_helper import int_input, yes_no_input
from output_helper import welcome

from art import LOGO

def main():
    print(LOGO)
    
    welcome('the secert auction program')

    participants = list()

    while True:
        
        participant = dict()

        name = input("What's your name: ")
        
        participant['name'] = name
        
        bid = int_input("What's you bid? ")
        participant['bid'] = bid
        
        participants.append(participant)
        
        should_continue = yes_no_input("Are there any other bidders? Type 'yes' or 'no': ")
        
        if not should_continue: break

    highest_bid = 0
    winner = ""

    for participant in participants:
        if highest_bid < participant['bid']:
            highest_bid = participant['bid']
            winner = participant['name']
            
    print(f'The winner is {winner} with a bid of {highest_bid}')
    
if __name__ == '__main__':
    main()