# Project Password Generator

import random

import sys
sys.path.append('../utils')
from input_helper import int_input, float_input
from output_helper import welcome


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def main():
    # first message
    welcome('the PyPassword Generator')
    
    # パスワードの仕様を確認
    num_letters = int_input('How many letters would you like in you password? ')
    num_numbers = int_input('How many numbers would you like? ')
    num_symbols = int_input('How many symbols would you like? ') 
    
    # パスワードの文字をを保存するリスト
    password = list()
    
    #　指定文字数分のそれぞれの文字をリストに追加
    password += choose(letters, num_letters)
    password += choose(numbers, num_numbers)
    password += choose(symbols, num_symbols)
    
    # 追加したものをシャッフル
    random.shuffle(password)
    
    # 文字列として表示
    print("".join(password))
    
    
    
def choose(char_list, num):
    passwd_char_list = list()
    for i in range(num):
        passwd_char_list.append(random.choice(char_list))
    return passwd_char_list

if __name__ == '__main__':
    main()