# Project Higher Lower

# The approach to solve the problem
# 1. Breakdown the problem
# 2. Make a Todo list
# 3. start with the easiest
# 4. Turn the problem into comments
# 5. Write code
# 6. Run code
# 7. Fix code
# ※repeat 5, 6, and 7 again and agein
# 8. Next Task

import random
import sys

sys.path.append('../utils')
from input_helper import int_input, yes_no_input
from output_helper import welcome

from art import TITLE_LOGO, VS_LOGO
from game_data import data

def main():
    
    # 飾り
    print(TITLE_LOGO)
    welcome('Game of Higher or Lower')
    
    # ポイントを記憶するように用意した変数
    current_score = 0
    
    while True:
        
        # ランダムな数を2つ生成
        random_num1 = random.randint(0, len(data))
        random_num2 = random.randint(0, len(data))
        
        # 選択肢Aを出力
        print_choice('a', random_num1)
        # フォロー数を記憶
        num_a_follower = data[random_num1]['follower_count']
        
        # 飾り
        print(VS_LOGO)
        
        # 選択肢Bを出力
        print_choice('b', random_num2)
        # フォロー数を記憶
        num_b_follower = data[random_num2]['follower_count']
        
        # 大きい方の選択肢のアルファベットを返す
        # HACK：関数名、インターフェースのリファクタリング
        answer_alpahbet = get_bigger_alphabet(num_choice_a=num_a_follower, num_choice_b=num_b_follower)
        
        # HACK：関数名のリファクタリング
        user_answer = a_or_b()
        
        
        if answer_alpahbet.lower() == user_answer.lower():
            current_score += 1
            print(f"You're right! Current score {current_score}")
        else:
            print(f"sorry, that's wrang. Final score: {current_score}")
            
            
        should_continue = input("Type 'q' to quit, Type 'n' to continue: ")
        
        if should_continue == 'q': break
        
    print('Bye👋')
    

def print_choice(a_or_b, random_num):
    
    # print関数の文字列を短くするために変数に入れただけ
    name = data[random_num]['name']
    description = data[random_num]['description']
    country = data[random_num]['country']
    
    print(f"Compare {a_or_b.upper()}:{name}, {description} , from {country}.")

# HACK：関数名のリファクタリング
def a_or_b():
    while True:
            user_answer = input("Who has more followers? Type 'A' or 'B': ")
            
            if user_answer.lower() == 'a' or user_answer.lower() == 'b': return user_answer
            else: print("You need to pick 'A' or 'B' ")

# HACK:関数名のリファクタリング
def get_bigger_alphabet(num_choice_a=0, num_choice_b=0):
    if num_choice_a > num_choice_b: return 'a'
    elif num_choice_b > num_choice_a: return 'b'
    else: return None

if __name__ == '__main__':
    main()