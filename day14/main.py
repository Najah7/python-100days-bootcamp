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
        
        # ランダムなアカウントを2つ
        accountA = random.choice(data)
        accountB = random.choice(data)
        
        # 選択肢Aのアカウント情報を出力
        # HACK:インターフェースのリファクタリング
        print_account_info('a', accountA)
        
        # 飾り
        print(VS_LOGO)
        
        # 選択肢Bのアカウント情報を出力
        # HACK:インターフェースのリファクタリング
        print_account_info('b', accountB)
        
        # 大きい方の選択肢のアルファベットを返す
        # HACK：関数名、インターフェースのリファクタリング
        answer_alpahbet = get_bigger_alphabet(num_a_follower=accountA['follower_count'], num_b_follower=accountB['follower_count'])
        
        # HACK：関数名のリファクタリング
        user_guess = a_or_b()
        
        
        if answer_alpahbet.lower() == user_guess.lower():
            current_score += 1
            print(f"You're right! Current score {current_score}")
        else:
            print(f"sorry, that's wrang. Final score: {current_score}")
            
            
        should_continue = input("Type 'q' to quit, Type 'n' to continue: ")
        
        if should_continue == 'q': break
        
    print('Bye👋')
    
# HACK:インターフェースのリファクタリング
def print_account_info(a_or_b, account):
    
    # print関数の文字列を短くするために変数に入れただけ
    name = account['name']
    description = account['description']
    country = account['country']
    
    print(f"Compare {a_or_b.upper()}:{name}, {description} , from {country}.")

# HACK：関数名のリファクタリング
def a_or_b():
    while True:
            user_guess = input("Who has more followers? Type 'A' or 'B': ")
            
            if user_guess.lower() == 'a' or user_guess.lower() == 'b': return user_guess
            else: print("You need to pick 'A' or 'B' ")

# HACK:関数名のリファクタリング
def get_bigger_alphabet(num_a_follower=0, num_b_follower=0):
    if num_a_follower > num_b_follower: return 'a'
    elif num_b_follower > num_a_follower: return 'b'
    else: return None

if __name__ == '__main__':
    main()