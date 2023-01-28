# This lecture for condition and Comparison Operators

# NOTE:conditionの例にお風呂の水が80cmたまったら止めて、
# たまってなかったらそのままというものを使っていた

# 仮想環境使ってないので、わざとこの記述をしている。
import sys
sys.path.append('../utils')
from input_helper import int_input, float_input, yes_no_input

APPS = ['Ticket Box', 'Odd or Even', 'BMI2.0', 'Leap Year', 'Pizza Order', 'Love Calculator']

def main():
    
    while(1):
        app = input('Select "Ticket Box", "Odd or Even", "BMI2.0", "Leap Year", "Pizza Order", "Love Calculator" ')
        
        if app in APPS: break

    # python 3.8を使ってるのでif文で
    if app == 'Ticket Box':
        print('Welcome to Ticket Box')
        ticket_box = TicketBox()

        height = ticket_box.ask_height()
    
        if height:
            ticket_box.calculate_cost_by_age()
            ticket_box.ask_extra_option('Do you want to take a photo?', 3)
            ticket_box.pirnt_cost()
            
            
    elif app == 'Odd or Even':
        print('Welcome to Odd or Even')
        num = int_input('input a num: ')

        num_checker = OddOrEven(num)
        
        num_checker.cehck_num()
        
        
    elif app == 'BMI2.0':
        print('Welcome to BMI2.0')
        height = float_input('How tall are you in m? ')
        weight = float_input('how many kilograms do you weigh in kg? ')
        new_bmi = NewBmi(height, weight)
        new_bmi.answer()
        
        
    elif app == 'Leap Year':
        print('Welcome to Leap Year')
        year = int_input('year: ')
        leap_year = LeapYear(year)
        
        if leap_year.is_leap_year():
            print('This is leap year 🐰')
        else: print('This is not leap year')
        
    
    elif app == 'Pizza Order':
        print('Welcome to Pizza Order')
        
        pizza_order = PizzaOrder()
        
        pizza_order.ask_order()
        pizza_order.print_bill()
        
    elif app == 'Love Calculator':
        print('Welcome to Love Calculator')
        
        your_name = input('what is your name? ').lower()
        partner_name = input('what is your partner? ').lower()
        
        love_calculator = LoveCalculator(your_name, partner_name)
        
        love_calculator.calculate_love()
        love_calculator.print_love_score()

        
        
        
        

    

class TicketBox:
    
    def __init__(self):
        # NOTE:初期値は果たして適切なのか？
        self._height = 0
        self._age = 0
        self._cost = 0
        
        
    def ask_height(self):

        while(1):
            
            self._height = float_input('How tall are you in m? ') 
                
            if self._height < 120:
                print("Sorry, you have to grow taller before you can ride.")
                self._height = 0
                break   
            
            return self._height
    
    def calculate_cost_by_age(self):
        self._age = int_input('How old are you? ')
        
        if self._age < 12:
            self._cost += 5
        elif 12 <= self._age <= 18:
            self._cost += 7
        else:
            self._cost += 12
        
    def ask_extra_option(self, message, fee):
        
        is_yes = yes_no_input(message)
        
        if is_yes:
            self._cost += fee
        
    def pirnt_cost(self):
        print(f'It will cost ${self._cost}')
            
        
class OddOrEven:
    def __init__(self, num):
        self._num = num
    
    # HACK: naming and maybe it should return value
    def cehck_num(self):
        if self._num % 2:
            print('This is odd')
        else: print('This is even')
        
class NewBmi:
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
        
    def bmi(self):
        return self._weight / (self._height **2)
    
    def print_bmi(self):
        print(self._bmi())

    def answer(self):
        bmi = self._bmi()
        print(bmi)
        if bmi < 18.5:
            print('You are underweight')
        elif bmi < 25:
            print('You are normal weight')
        elif bmi < 30:
            print('You are overweight')
        elif bmi < 35:
            print('You are obese')
        else:
            print('You are clinically obese')
        
class LeapYear:
    def __init__(self, year):
        self._year = year
        
    @staticmethod
    def is_divisiable(num, division):
        if num % division == 0: return True
        return False
    
    
    def is_leap_year(self):
        # うるう年の計算について：https://www.youtube.com/watch?v=xX96xng7sAE
        # NOTE:フォローチャートを使うと理解しやすい
        # calculate 3 rules of leap year
        divided_4 = self.is_divisiable(self._year, 4)
        divided_100 = self.is_divisiable(self._year, 100)
        divided_400 = self.is_divisiable(self._year, 400)
        
        # calculate if it is leap year
        if ((divided_4 and not divided_100) or divided_400): return True
        
        return False

class PizzaOrder:
    
    PEPPERONI_FEE = 3
    CHEESE_FEE = 1
    
    def __init__(self):
        self._total = 0
        self._size = ''
        self._pizza_sizes = {'S': 15, 'M': 20, 'L':25}
        self._add_pepperoni = False
        self._extra_cheese = False
        
    def ask_order(self):
        size = input("What size of pizza do you want? S, M or L ").upper()
        if size in self._pizza_sizes.keys():
            self._size = size
        else:
            print('choose a size in S, M or L ')
            
        
        self._add_pepperoni = yes_no_input('Do you want pepperoni? Y or N ')
        self._extra_cheese = yes_no_input('Do you want extara cheese? Y or N ')
    
    def print_bill(self):
        self._total += self._pizza_sizes[self._size]
        if self._add_pepperoni:
            self._total += self.PEPPERONI_FEE
        if self._extra_cheese:
            self._total += self.CHEESE_FEE
        print(f'Your final bill is ${self._total}')
        
        
class LoveCalculator:
    
    def __init__(self, your_name, partner_name):
        self._your_name = your_name
        self._partner_name = partner_name
        self._true = 'true'
        self._love = 'love'
        self._love_score = 0
        
    def calculate_love(self):
        
        first_digit = 0
        for letter in self._true:
            first_digit += self._your_name.count(letter)
            first_digit += self._partner_name.count(letter)
        
        second_digit = 0
        for letter in self._love:
            second_digit += self._your_name.count(letter)
            second_digit += self._partner_name.count(letter)
            
        self._love_score = int(str(first_digit) + str(second_digit))
        
    def print_love_score(self):
        if self._love_score < 10 or 90 < self._love_score:
            print(f'Your score is {self._love_score}, you go together like coke and mentos')
        elif 40 <= self._love_score <= 50:
            print(f'Your score is {self._love_score}, you are alright together.')
        else:
            print(f'Your score is {self._love_score}%')
    
if __name__ == '__main__':
    main()
