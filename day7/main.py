# Project Hangman

import random
import string
import math

from .hangman_art import STAGE, LOGO
from .hangman_words import WORD_LIST



def main():
    
    print(LOGO)

    lives = 6
    
    num_round = 0

    # choose a word.
    chosen_word = random.choice(WORD_LIST)
    word_lenght = len(chosen_word)
    
    # make a list of blanks
    display = ['_' for i in range(word_lenght)]

    while True:
        # get user's guess
        guess = input('Guess a letter: ').lower()

        num_round += 1
        
        is_correct_answer = False
        
        # check if user's answer is correct
        for position in range(word_lenght):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                is_correct_answer = True
        #  
        if not is_correct_answer:
            lives -= 1
            print_hangman(lives)
            print("It's not in the word. You lose a life.")
            if lives == 0:
                print('YOU LOSE 💀') 
                break
        
        print(f"{''.join(display)}")
        
        if '_' not in display:
            print('YOU WIN 🎉')
            break
    
    

def print_hangman(life):
    print(STAGE[life])   
    
    
if __name__ == '__main__':
    main()