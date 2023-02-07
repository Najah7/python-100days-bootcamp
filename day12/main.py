# Project Number Guessing Game

#This lecture is for the Scope of python

# NOTE:スコープの説明におウチを使っていた。（敷地内、敷地外）
# NOTE:pythonは関数の内、と関数の外だけ（ブロックスコープはない（if, for, whileなど））
# NOTE:global Statementで関数内の変数をグローバル変数にできる。
# NOTE:グローバル変数は定数の宣言に有用。定数は大文字で。

import random
import sys

sys.path.append('../utils')
from input_helper import int_input, yes_no_input
from output_helper import welcome

from art import LOGO

GUESS_MAX = 100

EASY_LEVEL_ATTEMPTS = 10
DIFFICULT_LEVEL_ATTEMPTS = 5

HIGH = 1
LOW = -1
SAME = 0

def main():
    # 最初のアウトプット（飾り）
    print(LOGO)
    welcome('the Number Guessing Game!')
    
    # ゲームの演出としてのアウトプット
    print(f"I'm thinking of a number between 1 and {GUESS_MAX}.")
    
    # 答えを用意
    global ANSWER
    ANSWER = generate_random_num()
    
    
    
    # 初期設定のループ（設定項目：難易度による予想回数）
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        
        num_attenmpts = get_attenmpts_by(difficulty)
        
        if num_attenmpts: break
        
    # ゲームロジックのループ
    while True:
    
        print(f"You have {num_attenmpts} attempts ramaining to guess the number.")
        
        guess = int_input('Make a guess: ')
        
        feedback = get_feedback_on(guess)
        
        print_message_by(feedback)
        
        if feedback == SAME: break
        else: num_attenmpts -= 1
        
        if num_attenmpts == 0:
            print("You've run out of guesses, you lose")
            break


def generate_random_num():
    return random.randint(1, GUESS_MAX)

def get_attenmpts_by(difficulty):
    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif  difficulty == 'hard':
        return  DIFFICULT_LEVEL_ATTEMPTS
    else:
        print('Invalid Input!')
        return False

def get_feedback_on(guess):
    if guess < ANSWER:
        return HIGH
    elif ANSWER < guess:
        return LOW
    else:
        return SAME
    
def print_message_by(feedback):
    if feedback == HIGH:
        print('High👆')
    elif feedback == LOW:
        print('LOW👇')
    else:
        print(f'You got it🎉 The answer was {ANSWER}.')
    

if __name__ == '__main__':
    while True:
        main()
        should_continue = yes_no_input('Do you want to play again? ')
        if not should_continue: break
    print('Bye👋')