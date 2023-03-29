"""
Project Tip Calculator
"""

# 仮想環境使ってないので、わざとこの記述をしている。
import sys
sys.path.append('../utils')
from input_helper import int_input, float_input

# options wihich is percentages of tip
PERCENTAGES = [10, 12, 15]

def main():
    print('Welcome to the Tip Calculator.')
    
    total = float_input("What was the total bill? ")
    
    # HACK：関数化したい（いい名前が浮かばないので保留）(main関数の中でmessageという名前を使うのはナンセンス)
    message = 'What percentage tip would you like to give?'
    for percentage in PERCENTAGES:
        message += f' {percentage},'
    message += '? '
    
    percentage = percentage_input(message)

    num_people = int_input("How many people to split the bill? ")

    total_with_tip = calculate_total_with_tip(total, percentage)
    
    each_person_total = caluculate_each_person_total(total_with_tip, num_people)
    
    print(f'Each person should pay: {each_person_total:.2f}')

            
def in_options(percentage):
    """選択肢の中にあるかを判定して、真偽値を返す関数"""
    
    if percentage in PERCENTAGES:
        return True
    else:
        print('You only can select a percentage in 10, 12, 15')
        return False

def percentage_to_float(num):
    """パーセンテージに変換する関数"""
    if not isinstance(num, int): return None
    else: return num / 100
  
def percentage_input(message):
    """パーセンテージの入力を受け付けて、小数のパーセンテージを返す関数"""
    float_percentage = None
    while not float_percentage:
        user_input = int_input(message)
        
        is_in_options = in_options(user_input)
        if is_in_options:
            float_percentage = percentage_to_float(user_input)
            return float_percentage
        else: 
            print(f'select a num in {PERCENTAGES[0]}, {PERCENTAGES[1]}, {PERCENTAGES[2]}')
        

def calculate_total_with_tip(total, percentage):
    """合計金額とパーセンテージを受け取って、チップを含めた合計金額を返す関数"""
    return total + total * percentage

def caluculate_each_person_total(total_with_tip, num_people):
    """合計金額と人数を受け取って、人数で割った金額を返す関数"""
    return total_with_tip / num_people

if __name__ == '__main__':
    main()