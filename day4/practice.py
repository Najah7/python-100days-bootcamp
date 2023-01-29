# This lesson for Randomistation, Module, List,

# NOTE:Mersenne twister：PRNG(Pseudo-Random Number Generator：疑似乱数生成器)の一つ。pythonで使われている。
# NOTE:乱数のおすすめ動画：https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

# NOTE:pyhtonのモジュール検索におすすめサイト：https://www.askpython.com/

# NOTE:listのindexの0はポインタからきてる。だからインデックス≒オフセット（先頭ポイントから）。マイナスが使えるということは、多分、双方向リストかな？

# NOTE:randomモジュールの使った関数
    # randint(start, end)、
    # random()←floatを返す。
    # random.choice(list)

import random
import time

import sys
sys.path.append('../utils')
from input_helper import int_input, float_input, yes_no_input

APPS = ["Heads or Tails", "Who's Paying", "Treasure Map" ]

def main():
    while(1):
        app = input('Select "Heads or Tails", "Who\'s Paying" "Treasure Map" ')
        
        if app in APPS: break
    
    if app == 'Heads or Tails':
        # first message
        print('Welcome to Heads or Tails')
        
        # get user's guess 
        user_input = input('Heads or Tails?')
        
        # toss a coin.
        head_or_tail = HeadOrTails()
        answer = head_or_tail.get_answer()
        
        # check if user's guess is correct
        if user_input.lower() == answer.lower():
            print('BINGO')
        else:
            print('Not match')
            
            
    elif app == "Who's Paying":
        # first message
        print('Welcome to Who\'s Paying')
        
        # get number of participant
        num_player = int_input('How many player will be attending? ')
        
        
        
        # get participant's names
        # HACK:最初のこのリストの初期化...（もっといい感じに書けそう）
        participant = list()
        for i in range(int(num_player)):
            participant.append(input(f'input name of player{i + 1}: '))
        
        # decide payer
        who_paying = WhoPaying(participant)
        payer = who_paying.get_payer()
        
        # output result
        print('.....')
        time.sleep(3)
        print(f'{payer}!! You need to pay!!')
        
    elif app == 'Treasure Map':
        
        # first message
        print('Welcome to Treasure Map 🪙')
        
        treasuremap = TreasureMap()
        treasuremap.pirnt_map()
        while(treasuremap._continue):
            treasuremap.ask_user_guess()
            treasuremap.pirnt_response()
            treasuremap.pirnt_map()
        

        
# データをまとめて扱いたいだけの簡易的なクラスなので、アクセスに関するところはあまり気にしていない。

class HeadOrTails:
    def __init__(self):
        self._answer = 'Head'
    
    def _toss_coin(self):
        random_int = random.randint(0, 1)
        if random_int == 0:
            self._answer = 'Head'
        else: self._answer = 'Tails'
        
    def get_answer(self):
        self._toss_coin()
        return self._answer
        
class WhoPaying:
    def __init__(self, participant_list):
        self._participant = participant_list
        self._num_people = len(participant_list)
        self._payer = ''

    def _decide_payer(self):
        payer = random.choice(self._participant)
        self._payer = payer
    
    def get_payer(self):
        self._decide_payer()
        return self._payer
        
class TreasureMap:
    def __init__(self):
        self._row1 = ['⬜️', '⬜️', '⬜️']
        self._row2 = ['⬜️', '⬜️', '⬜️']
        self._row3 = ['⬜️', '⬜️', '⬜️']
        self._map = [self._row1, self._row2, self._row3]
        self.__treasure_x = random.randint(0, 2)
        self.__treasure_y = random.randint(0, 2)
        self._user_guess_x = 0
        self._user_guess_y = 0
        self._continue = True
        
    def pirnt_map(self):
        for row in self._map:
            print(row)
    
    def is_correct_location(self):

        # HACK:長すぎる
        if self.__treasure_x == self._user_guess_x\
            and\
            self.__treasure_y == self._user_guess_y:
            self._map[self._user_guess_x][self._user_guess_y] = 'o' 
            return True
        else:
            self._map[self._user_guess_x][self._user_guess_y] = 'X' 
            return False
    
    def ask_user_guess(self):
        while(1):
            try:
                user_input = input('Where is treasure? ex) 1, 2: ')
                break
            except:
                print('Wrong input')
        
        location = user_input.split(', ')
        self._user_guess_x = int(location[0]) - 1
        self._user_guess_y = int(location[1]) - 1
    
    def pirnt_response(self):
        flg = self.is_correct_location()
        if flg:
            print('You find the Treasure!!👑')
            self._continue = False
        else: print('Not find')
        
        

if __name__ == '__main__':
    main()